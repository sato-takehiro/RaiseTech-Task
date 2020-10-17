$(function(){

		//navを初期状態で非表示する
		　//$(".p-nav").show();

		//ハンバーガーメニューをクリックしたときにアクティブモードにする
		  $('.hamburger-menu').on('click', function() {
			$(this).toggleClass('hamburger-menu-active')
		  })
		  /*HMは横幅が大きい時は非表示小さい時は表示、クリック時に開く←、横幅変化時に閉じる← */
		  /*NMは横幅が小さい時は非表示（トグルにしまっている）←大きい時は表示、*/
})
