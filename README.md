# آزمایشگاه مهندسی نرم‌افزار: آزمایش اول
اعضای گروه: علیرضا حیدری - حمیدرضا یعقوبی

# گزارش
ابتدا یک ریپازیتوری با نام SE_week1 درست کردیم.
![Screenshot from 2023-10-30 21-38-21](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/798c4d3e-9bca-4ef4-a16e-82e49fd3462d)

سپس برای محافظ یک rule برای مرج کردن branchهای مختلف اضافه کردیم:
![Screenshot from 2023-10-30 21-42-09](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/d091c93d-f7db-44ec-b480-f98ca120835d)
![Screenshot from 2023-10-30 22-04-37](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/9ca3fe78-2825-4bff-88c2-bd3591134862)

سپس با درست کردن یک token شخصی برای این مخزن، پروژه را کلون کردیم و برای تست یک فایل HelloWorld در یک برنچ به آن اضافه کردیم و مرج کردیم.
![Screenshot from 2023-10-30 21-55-54](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/c3bb7758-26b7-46b3-aadd-c2e39f8645d5)
![Screenshot from 2023-10-30 21-56-14](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/233002c0-5f92-4374-abb2-fa567e004952)
![Screenshot from 2023-10-30 21-56-36](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/721bd11b-56a1-48fb-a064-7bdda5f83c28)
![Screenshot from 2023-10-30 21-57-07](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/dbf22cb3-d9c0-4072-a3d2-485c149ab6fb)
![Screenshot from 2023-10-30 21-57-19](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/a6318dfa-fb17-4c15-a770-897ceeb59851)
حال کافیست تا نگاهی به پوشه .git بندازیم. در این پوشه اطلاعات مخزنمون همچون branch های موجود وجود دارد.
![Screenshot from 2023-10-30 22-00-21](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/32144a02-337c-4cd9-b3fb-4872b84b6b6b)
حال فایل .gitignore را درست کردیم تا پوشه اسکرین شات های مربوط به گزارش را در نظر نگیرد
![Screenshot from 2023-10-30 22-13-59](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/60fecf2a-1ed7-4ee0-a28b-f25849d48340)
![Screenshot from 2023-10-30 22-14-08](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/00d0bc4a-5085-4e42-b9bc-502411f38121)
حال یک branch به نام dev ایجاد می‌کنیم و سپس پایپ لاین اولیه خود را در آن اضافه می‌کنیم و در انتها تغییرات را مرج می کنیم

![Screenshot from 2023-10-30 22-24-25](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/76c4aec3-1b83-484a-b0c0-45af52d51e23)
![Screenshot from 2023-10-30 22-22-48](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/bae19125-b6c3-43ed-9e42-e0c0326d50bf)
![Screenshot from 2023-10-30 22-21-31](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/2efa0b5a-bae6-457f-b83a-08fe2324cb7e)
حال شرایطی برای به وجود آمدن conflict اعمال میکنیم. برای این کار قبل از این که main خود را آپدیت کنیم ابتدا یکی از کدهایی که میدونیم روی main وجود داره رو تغییر میدیم روی branch مورد نظر. بعد checkout می کنیم روی main و git pull میزنیم. سپس به برنج مورد نظر میریم و برنچ main رو باهاش مرج میکنیم. این کار کانلفیکت ایجاد میکنه. تصاویر این پروسه رو در عکس های زیر میتونید مشاهده کنید.
![Screenshot from 2023-10-30 22-40-53](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/dda89997-816e-4ae0-9cc9-6c5989966ed4)
![Screenshot from 2023-10-30 22-39-00](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/13716480-1069-4c04-b35e-e83d3f21afaa)
![Screenshot from 2023-10-30 22-38-55](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/49981028-fb96-4ef2-a431-d72ad0a94c56)
![Screenshot from 2023-10-30 22-38-46](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/9e453b64-3c68-452f-bbfc-065127ce1a18)
![Screenshot from 2023-10-30 22-38-42](https://github.com/hamidrezayaghobi/SL_week1/assets/59170724/7b9d4375-29c7-4f89-a492-85a7714625ad)
در ادامه, به پروژه ماژول های divide و multiply را اضافه می‌کنیم و در طی چندین کامیت و اضافه و مرج کردن برنچ هایی برای logging و floating support, کد را تکمیل می‌کنیم. پروسه کلی در عکس های زیر قابل مشاهده است:

![Screenshot Description](https://raw.githubusercontent.com/hamidrezayaghobi/SL_week1/master/screenshots/added_func.png)
![Screenshot Description](https://raw.githubusercontent.com/hamidrezayaghobi/SL_week1/master/screenshots/conf_code.png)
![Screenshot Description](https://raw.githubusercontent.com/hamidrezayaghobi/SL_week1/master/screenshots/resolve_conf.png)
![Screenshot Description](https://raw.githubusercontent.com/hamidrezayaghobi/SL_week1/master/screenshots/final_code.png)
![Screenshot Description](https://raw.githubusercontent.com/hamidrezayaghobi/SL_week1/master/screenshots/resolve_conf.png)

# پرسش

## پرسش یک
به طور کلی این پوشه اطلاعات مخزن رو ذخیره میکنه. بالاتر یه ls از داخلش رو نشون دادم. مثلا یه پوشه داره که وقتی pull میکنی اگر کسی branchای درست کرده باشه اطلاعاتش رو اون تو میزاره. یا مثلا پوشه refs همه کامیت ها یا referenceهای برنچ هارو نگه میداره

## پرسش دو
کلا مفهوم این هستش که کامیت ها و پول ریکوئست ها تاجای ممکن کوچک و مفهوم باشند. مثل تعریف کردن یک فانکشن که اگر طولانی باشه بهتره تبدیلش کنیم به چنتا فانکشن، اینجا هم اگر بهتره هر تغییرات معنادار کوچیکی که میدیم کامیت کنیم و وقتی تغییراتمون به اندازه یکسری تغییرات معنا دار در پروژه رسید، پول ریکوئست بدیم. این کار هم باعث منظم شدن میشه هم از سرگیجه گرفتن و کانسرنی کردن ریوور هم جلوگیری میکنه.

## پرسش سه
<div dir="rtl">
- **fetch**: این دستور تغییرات را از یک remote repository دریافت می‌کند ولی به صورت خودکار آن تغییرات را با کارهای local `merge` نمی‌کند. این به شما اجازه می‌دهد که قبل از `merge` تغییرات را ببینید.
- **pull**: این دستور یک `fetch` را انجام می‌دهد و سپس تغییرات دریافت‌شده را با branch فعلی شما `merge` می‌کند.
- **merge**: این دستور دو branch را با یکدیگر `merge` می‌کند.
- **rebase**: به جای `merge` تاریخچهٔ دو branch، `rebase` تغییرات یک branch را روی دیگری اعمال می‌کند. این باعث می‌شود تاریخچه‌ی گیت تمیزتر به نظر برسد.
- **cherry-pick**: این دستور اجازه می‌دهد که یک commit خاص از یک branch به branch دیگر منتقل شود.

## پرسش چهار

- **reset**: این دستور HEAD را به یک commit مشخص برمی‌گرداند. می‌تواند تغییرات را در working directory یا staging area حذف کند.
- **revert**: به جای حذف تاریخچه، یک commit جدید می‌سازد که تغییرات commit مورد نظر را معکوس می‌کند. این به شما اجازه می‌دهد که تغییرات یک commit را بدون تغییر در تاریخچه برگردانید.
- **restore**: این دستور به شما اجازه می‌دهد تا تغییرات در working directory یا staging area را به حالت قبل برگردانید.

## پرسش پنج

- **Stage**: وقتی تغییراتی را در فایل‌های خود اعمال می‌کنید، آن‌ها در حالت "تغییر داده‌شده" قرار می‌گیرند. وقتی آن تغییرات را "stage" می‌کنید، شما در واقع به گیت می‌گویید که این تغییرات را برای commit آماده کند.
- **stash**: این دستور تغییرات ناکامل شما را در یک لیست موقت ذخیره می‌کند، به شما امکان می‌دهد که به branch دیگری بروید. بعداً می‌توانید به تغییرات `stash` برگردید و بر روی کار خود ادامه دهید.

## پرسش شش

- **Snapshot**: در زبان گیت، `snapshot` به معنای ثبت وضعیت فعلی فایل‌ها و پوشه‌ها در یک زمان خاص است. 
- وقتی یک `commit` در گیت انجام می‌شود، گیت یک `snapshot` از تمام فایل‌های پروژه‌ی شما در آن لحظه می‌گیرد و آن `snapshot` را با یک شناسهٔ منحصر به فرد ذخیره می‌کند. هر `commit` در واقع به یک `snapshot` از پروژه‌ی شما اشاره دارد.



</div>



<div dir="rtl">

## تفاوت دستورهای `fetch`, `pull`, `merge`, `rebase` و `cherry-pick`

- **fetch**: این دستور تغییرات را از یک remote repository دریافت می‌کند ولی به صورت خودکار آن تغییرات را با کارهای local `merge` نمی‌کند. این به شما اجازه می‌دهد که قبل از `merge` تغییرات را ببینید.
- **pull**: این دستور یک `fetch` را انجام می‌دهد و سپس تغییرات دریافت‌شده را با branch فعلی شما `merge` می‌کند.
- **merge**: این دستور دو branch را با یکدیگر `merge` می‌کند.
- **rebase**: به جای `merge` تاریخچهٔ دو branch، `rebase` تغییرات یک branch را روی دیگری اعمال می‌کند. این باعث می‌شود تاریخچه‌ی گیت تمیزتر به نظر برسد.
- **cherry-pick**: این دستور اجازه می‌دهد که یک commit خاص از یک branch به branch دیگر منتقل شود.

## تفاوت دستورهای `reset`, `revert` و `restore`

- **reset**: این دستور HEAD را به یک commit مشخص برمی‌گرداند. می‌تواند تغییرات را در working directory یا staging area حذف کند.
- **revert**: به جای حذف تاریخچه، یک commit جدید می‌سازد که تغییرات commit مورد نظر را معکوس می‌کند. این به شما اجازه می‌دهد که تغییرات یک commit را بدون تغییر در تاریخچه برگردانید.
- **restore**: این دستور به شما اجازه می‌دهد تا تغییرات در working directory یا staging area را به حالت قبل برگردانید.

## منظور از stage و کاربرد دستور `stash`

- **Stage**: وقتی تغییراتی را در فایل‌های خود اعمال می‌کنید، آن‌ها در حالت "تغییر داده‌شده" قرار می‌گیرند. وقتی آن تغییرات را "stage" می‌کنید، شما در واقع به گیت می‌گویید که این تغییرات را برای commit آماده کند.
- **stash**: این دستور تغییرات ناکامل شما را در یک لیست موقت ذخیره می‌کند، به شما امکان می‌دهد که به branch دیگری بروید. بعداً می‌توانید به تغییرات `stash` برگردید و بر روی کار خود ادامه دهید.

## مفهوم `snapshot` و ارتباط آن با `commit`

- **Snapshot**: در زبان گیت، `snapshot` به معنای ثبت وضعیت فعلی فایل‌ها و پوشه‌ها در یک زمان خاص است. 
- وقتی یک `commit` در گیت انجام می‌شود، گیت یک `snapshot` از تمام فایل‌های پروژه‌ی شما در آن لحظه می‌گیرد و آن `snapshot` را با یک شناسهٔ منحصر به فرد ذخیره می‌کند. هر `commit` در واقع به یک `snapshot` از پروژه‌ی شما اشاره دارد.

</div>




