window.onload = function() {
            const loadingBar = document.getElementById('loading-bar');
            
            // 显示加载条
            loadingBar.classList.add('active');

            // 延迟后将加载条隐藏
            setTimeout(function() {
                loadingBar.style.transition = 'width 0.3s ease-out';  // 动画时间
                loadingBar.style.width = '0%';  // 隐藏加载条
            }, 500);  // 延迟 500ms 后隐藏
        };