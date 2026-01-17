 const container = document.getElementById('data-container');
// dataset 会自动处理 JSON 字符串
  const POST_DATA = JSON.parse(container.dataset.info);
  if (POST_DATA){
    document.getElementById('titleInput').value = POST_DATA.title || '';
    document.getElementById('descrInput').value = POST_DATA.description || '';

    if (POST_DATA.cover_url) {
      coverUrl = POST_DATA.cover_url;
      const img = document.getElementById('coverPreview');
      img.src = coverUrl;
      img.classList.remove('hidden');

      document.getElementById('imageInput').classList.add('hidden')
      document.getElementById('coverUrlInput').classList.add('hidden')
      document.getElementById('deleteCoverButton').classList.remove('hidden');
    }

    if (POST_DATA.category_id) {
      // 获取 input 元素
      const checkbox = document.getElementById('CategoryConditions');
      // 设置为开启
      checkbox.checked = true;
      document.getElementById('CategoryList').classList.remove('hidden');
      document.getElementById('Headline').value = POST_DATA.category_name;
    }
  };