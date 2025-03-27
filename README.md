# **Web Scraper: Automated Property Data Extraction**  
**A Selenium-based web scraper that collects structured real estate listings from ImóvelWeb (Brazil) and generates organized PDF reports.**

## **Key Features**  
- 🕷️ **Web Scraper**: Automates data extraction from [ImóvelWeb](https://www.imovelweb.com.br) using Selenium, including:  
  - Property titles, prices, and descriptions  
  - Addresses and condo fees (IPTU)  
  - Photo URLs (with automated right-click capture)  
- 📄 **PDF Reporting**: Generates clean, formatted PDFs with:  
  - Section-organized property details  
  - Link-preserved content  
  - Emoji/special character sanitization  
- 🤖 **Automation**: Handles CAPTCHAs via `seleniumbase` and simulates mouse clicks with `pyautogui`.  

## **Tech Stack**  
```python
Python | SeleniumBase | PyAutoGUI | FPDF | Regex
```  

## **Workflow**  
1. **Scraping**:  
   - Navigates listing pages  
   - Extracts property cards  
   - Clicks individual listings for detailed data  
2. **Data Processing**:  
   - Cleans text (removes emojis/special chars)  
   - Structures information into logical categories  
3. **PDF Generation**:  
   - Creates timestamped reports  
   - Preserves hyperlinks for photos  

## **Use Cases**  
- Real estate market analysis  
- Automated property comparison  
- Lead generation for agents  

## **Setup**  
```bash
pip install seleniumbase pyautogui fpdf pyperclip
```  

## **Example Output**  
```text
----------------------------------------
Título: Apartamento à venda, 80m²  
----------------------------------------
Preço de Venda: R$ 450.000  
----------------------------------------
Fotos:  
   https://example.com/photo1.jpg  
   https://example.com/photo2.jpg  
```  

## **Why This Project?**  
- Focused on Brazilian real estate market specifics  
- Bypasses anti-bot measures with UC mode  
- Lightweight alternative to APIs  

**Note**: Configure `output_path` in code for your system.  

---

### **Roadmap**  
- [ ] Add MongoDB/PostgreSQL storage  
- [ ] Integrate LLM for description analysis  
- [ ] Support for other Brazilian portals (QuintoAndar, Zap)  

**License**: MIT  

---

This description highlights:  
1. **Market specificity** (Brazil/ImóvelWeb)  
2. **Technical sophistication** (CAPTCHA handling, PDF gen)  
3. **Practical applications**  
4. **Clear next steps**  

Want me to add installation details or contribution guidelines?
