print("🤖 Welcome to St. Joseph's College of Engineering Chatbot")
print("Type 'bye' or 'exit' to stop\n")

while True:
    user = input("You: ").lower()
    responses = []

    # Exit
    if user in ["bye", "exit"]:
        print("Bot: Thank you for visiting SJCE. Goodbye 👋")
        break

    # Greetings
    if user in ["hi", "hello", "hey"]:
        responses.append("Hello! Welcome to St. College of Engineering 😊")

    # General College Information
    if "name of the college" in user:
        responses.append("The name of the college is St. Joseph's College of Engineering (SJCE).")

    if "located" in user:
        responses.append("St. Joseph's College of Engineering is located in OMR, Chennai, Tamil Nadu.")

    if "omr" in user:
        responses.append("Yes, the college is located on Old Mahabalipuram Road (OMR), Chennai.")

    if "address" in user:
        responses.append("St. Joseph's College of Engineering, OMR, Chennai - 600119, Tamil Nadu.")

    if "campus" in user:
        responses.append("The college has a modern campus located on OMR with excellent infrastructure.")

    if "established" in user:
        responses.append("The college was established in the year 1994.")
    
    if "website" in user:
        responses.append("www.stjosephs.ac.in")
    
    if "email" in user:
        responses.append("sjce@stjoseph.ac.in")
    
    if "autonomous" in user:
        responses.append("No, the college is not autonomous.")

    if "aicte" in user:
        responses.append("Yes, the college is approved by AICTE.")

    if "anna university" in user or "affiliated" in user:
        responses.append("Yes, the college is affiliated to Anna University, Chennai.")

    if "contact" in user:
        responses.append("You can contact the college through its official website and college office.")

    # Courses & Departments
    if "courses offered" in user:
        responses.append("The college offers UG and PG engineering courses.")

    if "ug course" in user or "ug courses" in user:
        responses.append("UG courses include CSE, IT, ECE, EEE, Cyber Security, AIML, and Mechanical Engineering.")

    if "pg course" in user or "pg courses" in user:
        responses.append("PG courses include MBA.")

    if "departments" in user or "department" in user:
        responses.append("Departments include CSE, IT, ECE, EEE, Mechanical, and Science & Humanities.")
    
    if "computer science" in user:
        responses.append("Yes, Computer Science Engineering is offered.")
    
    if "duration" in user:
        responses.append("UG courses are 4 years and PG courses are 2 years long.")
    
    if "apply for admission" in user:
        responses.append("Admissions are done through Anna University counselling and management quota.")
    
    if "admission process" in user:
        responses.append("Admission is based on merit, counselling, and eligibility criteria.")
    
    if "eligibility" in user:
        responses.append("Students must have completed 10+2 with Physics, Chemistry, and Mathematics.")
    
    if "cutoff" in user:
        responses.append("Cutoff varies each year depending on department and category.")
    
    if "lateral entry" in user:
        responses.append("Yes, lateral entry is available for diploma students.")
    
    if "management quota" in user:
        responses.append("Yes, management quota seats are available.")
    
    if "fee structure" in user:
        responses.append("Fees are as per Anna University norms.")
    
    if "scholarship" in user:
        responses.append("Yes, government and institutional scholarships are available.")
    
    if "installment" in user:
        responses.append("Yes, installment payment options are available.")
    
    if "academic facilities" in user:
        responses.append("Internet Facilities, Library Facilities, Book Bank Facilities, Class Rooms Facilities, Conference Halls Facilities")
    
    if "internet facilities" in user:
        responses.append("Our college campus including hostels is well connected through Optical Fiber Network with 500 Nodes in ring topology.")
    
    if "conference halls" in user:
        responses.append("Yes, All A/C halls are equipped with the latest teaching aids like LCD projector for conducting guest lectures, symposiums, seminars, etc.")
    
    if "laboratories" in user or "lab" in user:
        responses.append("Yes, we have well-equipped laboratories for all departments including CAD CAM Lab, Fluid Mechanics Lab, Communication Systems Lab, VLSI Lab, Power Electronics Lab, and many more.")
    
    if "wifi" in user:
        responses.append("Yes, Wi-Fi is available across the campus.")

    if "library" in user:
        responses.append("Yes, the college has a well-equipped library.")

    if "sports" in user:
        responses.append("Yes, indoor and outdoor sports facilities are available.")

    if "placement" in user:
        responses.append("Yes, the college has a dedicated placement cell.")

    if "companies" in user:
        responses.append("IT and core companies visit the campus for placements.")

    if "internship" in user:
        responses.append("Yes, internship support is provided.")
    
    if "academic calendar" in user:
        responses.append("The academic calendar follows Anna University guidelines.")

    if "internal mark" in user:
        responses.append("Internal marks are based on tests, assignments, and attendance.")

    if "exam pattern" in user:
        responses.append("Exams are conducted as per Anna University regulations.")

    if "revaluation" in user:
        responses.append("Yes, revaluation is available.")
    
    if "dining hall" in user:
        responses.append("Yes, Spacious mess is available with an area of 65,000 sqft including the dining hall, kitchen, ice cream parlour, bakery and all other facilities.")
    
    if "vegetarian food" in user:
        responses.append("Yes, Our vegetarian menu includes traditional South Indian dishes as well as tasty North Indian and Chinese dishes.")
   
    if "working hours" in user or "college timing" in user or "office timing" in user:
        responses.append("College working hours are usually from 7:50 AM to 3:00 PM.")
    
    if "diet" in user:
        responses.append("In the Diet vegetarian section we serve Nutritious soup and dishes with less salt. Low calorie food items like dry chapattis, dal, fresh vegetables salad and rice with rasam are served.")
    
    if "non-vegetarian food" in user:
        responses.append("Yes, Non vegetarian section is quite famous with variety of dishes prepared from Mutton, Chicken, Fish, Egg as well as Dry fish.")
    
    if "special lunch" in user:
        responses.append("We celebrate important festivals like Pongal, Ugadi, Ramzan, Ganesha Festival, Onam, Vijaya dasami, Deepavali and Christmas with special dishes.")
    
    if "care to sick students" in user:
        responses.append("As per prescription of doctor care will be taken for sick students. We serve hot water, rice malt, bread, milk, etc., as per the need.")
    
    if "hostel facilities" in user or "hostel" in user:
        responses.append("Laundromat facility, newspapers, intercom facility, monthly outings, separate hostel block for UG first year students, water heaters from October to February.")
    
    if "store facilities" in user or "store" in user or "shop" in user or "grocery" in user:
        responses.append("Our college has two grocery stores (one for boys & one for girls) with snacks, stationery items & medicines for student convenience.")
    
    if "open air theater" in user:
        responses.append("There are two open air theatres - one near boys hostel and one near girls hostel for films and cultural activities.")
    
    if "indoor auditorium" in user:
        responses.append("We have a 35,000 sq.ft indoor auditorium with fully inbuilt sound system and lighting for convocation, college day and indoor games.")
    
    if "worship" in user or "temple" in user or "church" in user or "mosque" in user:
        responses.append("There is a fully air conditioned Church, Mosque and Temple each available for worship, prayer and meditation.")
    
    if "bank" in user:
        responses.append("Indian bank extension counter is available in the campus. Bank account is compulsory for all hostel students.")
    
    if "atm" in user:
        responses.append("Two ATM is available inside the campus which is a 24 hour facility.")
    
    if "beauty parlour" in user:
        responses.append("The parlour is equipped with all modern facilities and air-conditioned. Hostel students & staff can get services for free after college hours.")
    
    if "gym facilities" in user:
        responses.append("We have Basic gym, Advanced gym, Womens gym, Fitness & Physiotherapy")
    
    if "basic gym" in user:
        responses.append("Basic gym mainly designed for beginners with sufficient weight training equipments and dumbles with well trained trainers.")
    
    if "advanced gym" in user:
        responses.append("This gym designed for sports man, body builders with imported equipments and hydraulic coaches.")
    
    if "womens gym" in user:
        responses.append("Special gym for women focusing on weight loss, general fitness and strengthening.")
    
    if "fitness & physiotherapy" in user:
        responses.append("Physical therapy and rehabilitation center for pain management, posture corrections and sports injuries treatment.")
    
    if "abhs" in user:
        responses.append("The Advisory Bureau for Higher Studies (ABHS) serves students for getting higher studies admission in India and abroad with information on GRE, TOEFL, GMAT, IELTS, GATE and CAT.")
    
    if "dispensary" in user or "medical facilities" in user or  "hospital" in user:
        responses.append("Dr.K.Santhanam B.sc, MBBS, A full time medical officer is appointed. Medical center with 10 beds provides first aid and medical care round the clock at free of cost.")
    
    if "water purification" in user or "water" in user:
        responses.append("Drinking water is purified by modern treatment technology using Filtration, Ion exchange and Reverse osmosis with water coolers at various locations.")
    
    if "rewards" in user:
        responses.append("Rs.3 crore")
    
    if "placement empowerment program" in user or "pep" in user:
        responses.append("PEP (Placement Empowerment Programme) is a career-focused training initiative to equip students with practical, industry-relevant skills for interviews and technical roles.")
    
    if "pep domains" in user:
        responses.append("CAD and 3D Printing, AI and ML, Blockchain, Cloud Computing, Cyber Security, Data Science, DevOps, IoT, Full Stack Development, Japanese/Spanish Language, Mobile App Development, Robotics, UI/UX Design, VLSI Design, AR/VR Technology")
    
    if "hope" in user or "house of programming expertise" in user:
        responses.append("HOPE aims to make students good at solving programming problems for technical interviews and placements in top IT companies with focus on coding concepts and competitive programming.")
    
    if "saturday" in user:
        responses.append("The college may be open on Saturdays for special activities.")
    
    if "grievance" in user:
        responses.append("Yes, the college has a grievance redressal cell.")
    
    if "attendance" in user:
        responses.append("A minimum of 75% attendance is required.")
    
    if "anti ragging" in user:
        responses.append("Yes, there is a strict anti-ragging committee.")
    
    if "cultural" in user:
        responses.append("Yes, cultural events are conducted regularly.")
    
    if "mobile phone" in user:
        responses.append("Mobile is not allowed inside the college.")
    
    if "symposium" in user:
        responses.append("Yes, technical symposiums are conducted by departments.")

    if "clubs" in user:
        responses.append("Technical, cultural, sports, and social clubs are available.")

    if "nss" in user or "ncc" in user:
        responses.append("Yes, NSS and NCC programs are available.")

    if "workshops" in user:
        responses.append("Yes, workshops are conducted.")

    # Staff & Faculty
    if "staff" in user or "faculty" in user:
        responses.append("The college has qualified and experienced faculty members across all departments with Ph.D. and M.E./M.Tech qualifications.")

    if "teachers" in user or "professors" in user:
        responses.append("Highly qualified professors and assistant professors with industry and research experience teach in various departments.")

    if "hod" in user or "head of department" in user:
        responses.append("Each department has an experienced Head of Department (HOD) with extensive academic and research credentials.")

    if "principal" in user:
        responses.append("Dr.Vaddi Seshagiri Rao M.E., M.B.A., Ph.D")
    
    if "chairman" in user:
        responses.append("Dr.B.Babu Manoharan M.A., MBA., Ph.D")
    
    if "managing director" in user:
        responses.append("Mr. B. Shashi Sekar M.sc., INTL.Business")
    
    if "executive director" in user:
        responses.append("Mrs. S. Jessie Priya M.Com")
    
    if "faculty qualification" in user or "staff qualification" in user:
        responses.append("Faculty members hold Ph.D., M.E., M.Tech, and MBA degrees from reputed institutions.")

    if "faculty experience" in user:
        responses.append("Faculty members have extensive teaching and industry experience ranging from 5 to 20+ years.")

    
    if "bus" in user or "transport" in user:
        responses.append("Yes, college bus facilities are available from various parts of Chennai with safe and comfortable travel.")

    if "bus routes" in user or "route" in user:
        responses.append("Bus routes cover Tambaram, Velachery, Chrompet, Pallavaram, Perungalathur, Guduvanchery, Avadi, Mogappair, Redhills, Villivakkam, and other major areas in Chennai.")

    if "bus timing" in user:
        responses.append("College buses operate from 6:30 AM onwards with pickup services and return after college hours around 3:30 PM.")

    if "bus fee" in user or "transport fee" in user:
        responses.append("Bus fees vary from Rs. 15,000 to Rs. 25,000 per year based on distance and route. Contact transport office for exact details.")

    if "bus facility" in user:
        responses.append("College provides well-maintained buses with GPS tracking and experienced drivers for student safety.")

    # Training & Development
    if "trainers" in user or "training" in user or "training program" in user:
        responses.append("The college provides training through qualified trainers, industry experts, and certified professionals in various domains.")

    if "skill development" in user or "skills" in user:
        responses.append("Skill development programs include coding bootcamps, soft skills training, aptitude training, and technical workshops conducted by expert trainers.")

    if "industry training" in user or "corporate training" in user:
        responses.append("Industry training sessions are organized with professionals from TCS, Infosys, Wipro, Cognizant, and other leading companies.")

    if "certification" in user or "certificate course" in user:
        responses.append("Certification courses are available in Python, Java, Cloud Computing, Data Science, AI/ML, Cyber Security with qualified trainers.")

    if "placement training" in user:
        responses.append("Placement training includes aptitude, technical interviews, group discussions, and HR interview preparation by experienced trainers.")

    if "workshop" in user:
        responses.append("Regular workshops on emerging technologies are conducted by industry trainers and academic experts.")

    # Food & Canteen
    if "food" in user or "canteen" in user or "mess" in user:
        responses.append("St. Joseph's College of Engineering has a spacious canteen serving fresh, hygienic food with both vegetarian and non-vegetarian options.")

    if "veg" in user or "vegetarian" in user:
        responses.append("Vegetarian menu includes idli, dosa, sambar rice, curd rice, chapati, dal, vegetable curry, biriyani, and various South Indian snacks.")

    if "non veg" in user or "non-veg" in user or "nonveg" in user:
        responses.append("Non-vegetarian items include chicken curry, chicken biriyani, mutton curry, fish fry, egg curry, and chicken fried rice.")

    if "breakfast" in user:
        responses.append("Breakfast options include idli, dosa, vada, upma, pongal, bread toast, and various tiffin items from 8:00 AM to 10:00 AM.")

    if "lunch" in user:
        responses.append("Lunch is served from 12:30 PM to 2:00 PM with rice varieties, sambar, rasam, vegetables, curd, and non-veg options.")

    if "snacks" in user:
        responses.append("Evening snacks include samosa, bajji, bonda, sandwich, puffs, biscuits, and tea/coffee available throughout the day.")

    if "food quality" in user:
        responses.append("The canteen maintains excellent food quality with fresh ingredients, proper hygiene standards, and regular health inspections.")

    if "food price" in user or "canteen price" in user:
        responses.append("Food prices: Breakfast Rs. 15-25, Lunch Rs. 40-60, Snacks Rs. 10-20, Beverages Rs. 8-15. Very affordable for students.")

    # Girls Safety
    if "girls safety" in user or "women safety" in user or "female safety" in user:
        responses.append("The college ensures complete safety for female students with 24/7 security, CCTV surveillance, and women's cell support.")

    if "women cell" in user or "girls committee" in user:
        responses.append("Active Women's Cell addresses grievances and ensures a safe, harassment-free environment for female students.")

    if "security" in user:
        responses.append("Round-the-clock security personnel, CCTV cameras, and restricted entry ensure campus safety for all students.")

    if "cctv" in user or "surveillance" in user:
        responses.append("Comprehensive CCTV surveillance system covers all areas including classrooms, corridors, and common areas for student safety.")

    if "harassment" in user:
        responses.append("Zero tolerance policy for harassment with immediate action through Women's Cell and disciplinary committee.")
    
    # Output responses
    if responses:
        for response in responses:
            print(f"Bot: {response}")
    else:
        print("Bot: Sorry, I didn't understand your question. Please try again.")