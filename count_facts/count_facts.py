import PySide2.QtWidgets as QT

kazennye_sady =     {
                    'd90b5df8-54b2-4a88-9302-fe35c3a08f44':
                        [
                        '42e266b6-85d9-438a-88d3-c738c9b526c9',
                        'e1cbbbc9-0113-4623-bbd6-56fa32185020'
                        ],
                    'cef59820-c062-489b-a43e-7eca1089a5be':
                        [
                        '42e266b6-85d9-438a-88d3-c738c9b526c9',
                        'e1cbbbc9-0113-4623-bbd6-56fa32185020'
                        ],
                    'dbbbeafb-590b-4bdf-97a2-569a8afe6d7f':
                        [
                        '195743f6-fbc7-41eb-b889-873080844551'
                        ],
                    '4b120a4b-b68c-436d-a24d-fc62683e46bb':
                        [
                        'cfa1fd65-68a3-467a-9c28-326505dea170',
                        '5d4cc54b-97c4-4b46-b4ba-934455401602',
                        '76f09c67-b776-4967-8f30-65761c0df705',
                        '23583086-5535-4808-b55c-5318a43ee56e'
                        ]
                    }
budjetnye_sady =    {
                    '17f046ea-a5e5-49b3-a75a-b13f832bea2b':
                        [
                        '42e266b6-85d9-438a-88d3-c738c9b526c9',
                        'e1cbbbc9-0113-4623-bbd6-56fa32185020'
                        ],
                    'dbbbeafb-590b-4bdf-97a2-569a8afe6d7f':
                        [
                        '195743f6-fbc7-41eb-b889-873080844551'
                        ],
                    '4b120a4b-b68c-436d-a24d-fc62683e46bb':
                        [
                        'cfa1fd65-68a3-467a-9c28-326505dea170',
                        '5d4cc54b-97c4-4b46-b4ba-934455401602',
                        '76f09c67-b776-4967-8f30-65761c0df705',
                        '23583086-5535-4808-b55c-5318a43ee56e'
                        ]
                    }
kazennye_shkoly=    {
                    '6f712658-3040-4402-82c8-a71eddf15513':
                        [
                        '42e266b6-85d9-438a-88d3-c738c9b526c9',
                        'e1cbbbc9-0113-4623-bbd6-56fa32185020'
                        ],
                    'ccf49282-8cb1-4fd1-93a3-4acff183bcd8':
                        [
                        '42e266b6-85d9-438a-88d3-c738c9b526c9',
                        'e1cbbbc9-0113-4623-bbd6-56fa32185020'
                        ],
                    'df7a014d-a8bc-411d-b103-ad105d94f24e':
                        [
                        'd0cd91d0-6101-4a03-8e0b-32ce45b1cae3'
                        ]
                    }
budjetnye_shkoly =    {
                    'ea4ca0d2-65eb-4b9b-980a-7a804ab40731':
                        [
                        '42e266b6-85d9-438a-88d3-c738c9b526c9',
                        'e1cbbbc9-0113-4623-bbd6-56fa32185020'
                        ],
                    'df7a014d-a8bc-411d-b103-ad105d94f24e':
                        [
                        'd0cd91d0-6101-4a03-8e0b-32ce45b1cae3'
                        ]
                    }
dopy =              {
                    '5c64e81d-db3b-4f00-8c22-681e48d1d329':
                        [
                        '42e266b6-85d9-438a-88d3-c738c9b526c9',
                        'e1cbbbc9-0113-4623-bbd6-56fa32185020'
                        ]
                    }
opeka =            {
                    '324d6e47-f1f0-478e-83ee-aeb40c3817dd':
                        [
                        'f63bd6f9-5975-4cff-908e-e595db596c80'
                        ],
                    '36c2a946-0bb7-4b1a-a2bf-d947b6f1019c':
                        [
                        'f63bd6f9-5975-4cff-908e-e595db596c80'
                        ]
                    }
kultura =          {
                    '34a0ac95-a8db-4a94-bc27-8e2eff70db25':
                        [
                        '908f30cc-b7ca-4da4-88c8-f1b12808a4fa'
                        ],
                    '7c48ccc0-d936-4043-83af-1fd039ca1049':
                        [
                        '2f5ecd8c-2096-4c00-82e8-efcae71b4316'
                        ],
                    '4630ba88-0367-4c64-9bc9-4b721055b502':
                        [
                        '46c3f433-e219-4b39-9170-a9aa01a49485'
                        ],
                    '7c89a01d-b4ce-4b10-bb01-44e9abde230d':
                        [
                        'e1cbbbc9-0113-4623-bbd6-56fa32185020'
                        ]
                    }

if __name__ == "__main__":
    app = QT.QApplication()

    facts = []
    facts += list(kazennye_sady)
    facts += list(budjetnye_sady)
    facts += list(kazennye_shkoly)
    facts += list(budjetnye_shkoly)
    facts += list(dopy)
    facts += list(opeka)
    facts += list(kultura)

    pitanye_fact = ['df7a014d-a8bc-411d-b103-ad105d94f24e']

    facts_stat = {
        'num': 0,
        'sum': 0
    }

    msgBox = QT.QMessageBox(text="The document has been modified.")
    msgBox.exec()