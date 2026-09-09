# Joan Achieng Abwao – Portfolio

Professional portfolio website for **Joan Achieng Abwao**, Agricultural Statistician & Data Analyst at the Kenya Agricultural and Livestock Research Organization – Horticulture Research Institute (KALRO-HRI).

This static site showcases selected statistical analyses, crop and livestock research support, market studies, surveys, training activities and publications.

**Live demo (after you enable GitHub Pages):**  
`https://abwaojoan.github.io/joan-abwao-portfolio/`

---

## Features

- Clean, modern, responsive single-page design
- Sections: Hero, About, Skills, Projects (filterable), Publications, Contact
- Mobile-friendly navigation
- Project filter buttons (Statistical Analysis, Livestock, Crops & Soil, Market & Economics, Surveys & Training)
- Professional colour palette inspired by agriculture (greens + warm accent)

---

## How to use this portfolio on GitHub

### 1. Create a new repository

1. Go to [GitHub](https://github.com/new)
2. Name it `joan-abwao-portfolio`
3. Make it **Public**
4. Do **not** initialize with a README (we already have one)

### 2. Upload the files

**Option A – GitHub website (easiest)**

1. Open the new empty repository
2. Click **Add file → Upload files**
3. Drag and drop **all** the contents of this folder (`index.html`, `css/`, `js/`, `assets/`, `README.md`)
4. Commit the changes

**Option B – Git command line**

```bash
git clone https://github.com/abwaojoan/joan-abwao-portfolio.git
cd joan-abwao-portfolio
# copy all files from this portfolio folder into the repo
git add .
git commit -m "Initial portfolio site"
git push origin main
```

### 3. Enable GitHub Pages

1. In your repository go to **Settings → Pages**
2. Under **Source** select **Deploy from a branch**
3. Choose branch `main` (or `master`) and folder `/ (root)`
4. Click **Save**
5. After a minute or two your site will be live at:  
   `https://abwaojoan.github.io/joan-abwao-portfolio/`

---

## Customisation

- **Photo**: Replace `assets/photo.jpg` with your preferred professional photo (recommended ~600×680 px).
- **Email / contact**: Edit the contact section in `index.html`.
- **Projects**: Add, remove or edit the project cards inside the `#projects` section.
- **Colours**: Adjust the CSS variables at the top of `css/styles.css`.

---

## Project structure

```
joan-abwao-portfolio/
├── index.html          # Main page
├── css/
│   └── styles.css      # All styles
├── js/
│   └── main.js         # Navigation + project filters
├── assets/
│   └── photo.jpg       # Profile photo
└── README.md           # This file
```

---

## Licence

This portfolio template is free for personal and professional use.  
The underlying research reports and data remain the property of KALRO and collaborating institutions.

---

**Joan Achieng Abwao**  
KALRO – Horticulture Research Institute  
Email: abwaojoan3@gmail.com
