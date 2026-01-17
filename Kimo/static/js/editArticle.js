const postId =POST_DATA.id;
    console.log(postId);

  document.getElementById('editBtn').addEventListener('click', async () => {
      const title = document.getElementById('titleInput').value.trim();
      const content = vditor.getValue().trim();
      const coverUrl = document.getElementById("coverPreview").src;
      const description = document.getElementById('descrInput').value.trim();
      const description_result = description.trim() === '' ? null : description.trim();
      const categoryToggle = document.getElementById('CategoryConditions').checked
      if (!title) {
        showModal('标题不能为空');
        return;
      }
      if (!content) {
        showModal('内容不能为空');
        return;
      }
      if (!postId) {
        showModal('id is empty');
        return;
      }
      if (!categoryToggle) {
        category_name = null;
      }
      else{
        category_name = document.getElementById('Headline').value;
      }
 const res = await fetch('/articles/update', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ title, content ,category_name,description_result,coverUrl , postId})
});

const data = await res.json();

if (res.ok) {
  showModal('编辑成功');
  vditor.setValue('');

  setTimeout(() => {
    window.location.href = '/';
  }, 800);
} else {
  showModal(data.message || '编辑失败');
}
    });