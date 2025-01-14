UR5E_ROBOTIQ_CONSTANTS=dict(
    name="ur5e_robotiq",
    all_joint_names=[
        "ur5e_0_shoulder_pan_joint",
        "ur5e_0_shoulder_lift_joint",
        "ur5e_0_elbow_joint",
        "ur5e_0_wrist_1_joint",
        "ur5e_0_wrist_2_joint",
        "ur5e_0_wrist_3_joint",
        "ur5e_0_base_joint", 
        ],
    ik_joint_names=[
        "ur5e_0_shoulder_pan_joint",
        "ur5e_0_shoulder_lift_joint",
        "ur5e_0_elbow_joint",
        "ur5e_0_wrist_1_joint",
        "ur5e_0_wrist_2_joint",
        "ur5e_0_wrist_3_joint",
        "ur5e_0_base_joint", 
    ],
    arm_joint_names=[
        "ur5e_0_shoulder_pan_joint",
        "ur5e_0_shoulder_lift_joint",
        "ur5e_0_elbow_joint",
        "ur5e_0_wrist_1_joint",
        "ur5e_0_wrist_2_joint",
        "ur5e_0_wrist_3_joint",
        ],
    actuator_info={
        "ur5e_0_shoulder_pan_joint": "ur5e_0_shoulder_pan",
        "ur5e_0_shoulder_lift_joint": "ur5e_0_shoulder_lift",
        "ur5e_0_elbow_joint": "ur5e_0_elbow",
        "ur5e_0_wrist_1_joint": "ur5e_0_wrist_1",
        "ur5e_0_wrist_2_joint": "ur5e_0_wrist_2",
        "ur5e_0_wrist_3_joint": "ur5e_0_wrist_3",
        "ur5e_0_base_joint": "ur5e_0_base",
        },
    all_link_names=[
        "ur5e_0_shoulder_link",
        "ur5e_0_upper_arm_link",
        "ur5e_0_forearm_link",
        "ur5e_0_wrist_1_link",
        "ur5e_0_wrist_2_link",
        "ur5e_0_wrist_3_link",
        "ur5e_0_robotiq_gripper",
        "robotiq_base_mount",
        "2f85_base",
        "right_driver",
        "right_spring_link",
        "right_pad",
        "right_follower",
        "right_coupler", 
        "left_driver",
        "left_spring_link",
        "left_pad", 
        "left_follower",
        "left_coupler", 
        ],
    arm_link_names=[
        "ur5e_0_shoulder_link",
        "ur5e_0_upper_arm_link",
        "ur5e_0_forearm_link",
        "ur5e_0_wrist_1_link",
        "ur5e_0_wrist_2_link",
        "ur5e_0_wrist_3_link", 
        ],
    ee_link_names=[
        "right_driver",
        "right_spring_link",
        "right_pad",
        "right_follower",
        "right_coupler", 
        "left_driver",
        "left_spring_link",
        "left_pad", 
        "left_follower",
        "left_coupler"
        ], 
    base_joint="ur5e_0_base_joint",
    ee_site_name="robotiq_ee",
    grasp_actuator="robotiq_fingers_actuator",
    weld_body_name="robotiq",
)

UR5E_SUCTION_CONSTANTS=dict(
    name="ur5e_suction",
    all_joint_names=[
        "ur5e_1_shoulder_pan_joint",
        "ur5e_1_shoulder_lift_joint",
        "ur5e_1_elbow_joint",
        "ur5e_1_wrist_1_joint",
        "ur5e_1_wrist_2_joint",
        "ur5e_1_wrist_3_joint",
        "ur5e_1_base_joint",
        ],
    ik_joint_names=[
        "ur5e_1_shoulder_pan_joint",
        "ur5e_1_shoulder_lift_joint",
        "ur5e_1_elbow_joint",
        "ur5e_1_wrist_1_joint",
        "ur5e_1_wrist_2_joint",
        "ur5e_1_wrist_3_joint",
        "ur5e_1_base_joint",        
    ],
    arm_joint_names=[
        "ur5e_1_shoulder_pan_joint",
        "ur5e_1_shoulder_lift_joint",
        "ur5e_1_elbow_joint",
        "ur5e_1_wrist_1_joint",
        "ur5e_1_wrist_2_joint",
        "ur5e_1_wrist_3_joint", 
        ],
    actuator_info={
        "ur5e_1_shoulder_pan_joint": "ur5e_1_shoulder_pan",
        "ur5e_1_shoulder_lift_joint": "ur5e_1_shoulder_lift",
        "ur5e_1_elbow_joint": "ur5e_1_elbow",
        "ur5e_1_wrist_1_joint": "ur5e_1_wrist_1",
        "ur5e_1_wrist_2_joint": "ur5e_1_wrist_2",
        "ur5e_1_wrist_3_joint": "ur5e_1_wrist_3",
        "ur5e_1_base_joint": "ur5e_1_base",
        },
    all_link_names=[
        "ur5e_1_shoulder_link",
        "ur5e_1_upper_arm_link",
        "ur5e_1_forearm_link",
        "ur5e_1_wrist_1_link",
        "ur5e_1_wrist_2_link",
        "ur5e_1_wrist_3_link",
        "ur5e_1_suction_gripper",
        "suction_base",
        "suction_midLink",
        "suction_headLink",
        "suction_tipLink",
        "suction_disk",
        ],
    arm_link_names=[
        "ur5e_1_shoulder_link",
        "ur5e_1_upper_arm_link",
        "ur5e_1_forearm_link",
        "ur5e_1_wrist_1_link",
        "ur5e_1_wrist_2_link",
        "ur5e_1_wrist_3_link", 
        ],
    ee_link_names=["suction_headLink", "suction_tipLink", "suction_disk"],
    base_joint="ur5e_1_base_joint",
    ee_site_name="suction_ee",
    grasp_actuator="adhere_gripper",
    weld_body_name="suction",
)
PANDA_CONSTANTS=dict(
    name="panda",
    all_joint_names=[
        "panda_joint1",
        "panda_joint2",
        "panda_joint3",
        "panda_joint4",
        "panda_joint5",
        "panda_joint6",
        "panda_joint7",
        "panda_finger_joint1",
        "panda_finger_joint2",
        "panda_base_joint",
        ],
    ik_joint_names=[
        "panda_joint1",
        "panda_joint2",
        "panda_joint3",
        "panda_joint4",
        "panda_joint5",
        "panda_joint6",
        "panda_joint7", 
        "panda_base_joint",
    ],
    arm_joint_names=[
        "panda_joint1",
        "panda_joint2",
        "panda_joint3",
        "panda_joint4",
        "panda_joint5",
        "panda_joint6",
        "panda_joint7",
        ],
    actuator_info={
        "panda_joint1": "panda_actuator1",
        "panda_joint2": "panda_actuator2",
        "panda_joint3": "panda_actuator3",
        "panda_joint4": "panda_actuator4",
        "panda_joint5": "panda_actuator5",
        "panda_joint6": "panda_actuator6",
        "panda_joint7": "panda_actuator7",
        "panda_base_joint": "panda_base",
        "split": "panda_gripper_actuator",
    },
    grasp_actuator="panda_gripper_actuator",
    all_link_names=[
        "panda_link0",
        "panda_link1",
        "panda_link2",
        "panda_link3",
        "panda_link4",
        "panda_link5",
        "panda_link6",
        "panda_link7",
        "panda_hand",
        "panda_left_finger",
        "panda_right_finger",
        ],
    arm_link_names=[
        "panda_link0",
        "panda_link1",
        "panda_link2",
        "panda_link3",
        "panda_link4",
        "panda_link5",
        "panda_link6",
        "panda_link7",
        ],
    ee_link_names=["panda_hand", "panda_left_finger", "panda_right_finger"],
    base_joint="panda_base_joint",
    ee_site_name="panda_ee",
    weld_body_name="panda",
)

HUMANOID_CONSTANTS=dict(
    name="humanoid",
    all_joint_names=[
        "human_base_joint",
        "thoraxry",
        "thoraxrx",
        "rclaviclery",
        "rclaviclerz",
        "rhumerusrx",
        "rhumerusry",
        "rhumerusrz", 
        "rradiusrx",
        "rwristry", 
        "rhandrx",
        "rhandrz",
        "rfingersrx",
        "rthumbrx",
        "rthumbrz",   
    ],
    ik_joint_names=[
        "human_base_joint",
        "thoraxry",
        "thoraxrx",
        "rclaviclery",
        "rclaviclerz",
        "rhumerusrx",
        "rhumerusry",
        "rhumerusrz", 
        "rradiusrx",
        "rwristry", 
        "rhandrx",
        "rhandrz",    
    ],
    arm_joint_names=[
        "thoraxry",
        "thoraxrz",
        "rclaviclery",
        "rclaviclerz",
        "rhumerusrx",
        "rhumerusry",
        "rhumerusrz", 
        "rradiusrx",
        "rwristry", 
        "rhandrx",
        "rhandrz",    
        ],
    actuator_info={
        "human_base_joint": "human_base",
        "rhumerusrx": "rhumerusrx",
        "rhumerusry": "rhumerusry",
        "rhumerusrz": "rhumerusrz",
        "rclaviclery": "rclaviclery",
        "rclaviclerz": "rclaviclerz",
        "rradiusrx": "rradiusrx",
        "rhandrx": "rhandrx",
        "rhandrz": "rhandrz",
        "rwristry": "rwristry",
        "rfingersrx": "rfingersrx",
        "thoraxrx": "thoraxrx",
        "thoraxry": "thoraxry",
        "thoraxrz": "thoraxrz",
        "rthumbrx": "rthumbrx",
        "rthumbrz": "rthumbrz", 
        "fingers": ["rfingersrx", "rthumbrz"],
        },
    grasp_actuator="adhere_hand",
    all_link_names=[
        "lowerback",
        "upperback",
        "thorax",
        "lowerneck",
        "upperneck",
        "head",
        "lclavicle",
        "lhumerus",
        "lradius",
        "lhand",
        "lfingers",
        "lthumb",
        "rclavicle",
        "rhumerus",
        "rradius",
        "rhand",
        "rfingers",
        "rpalm",
        "rthumb",
        ],
    arm_link_names=[
        "upperback",
        "thorax",
        "lowerneck",
        "upperneck",
        "head",
        "rclavicle",
        "rhumerus",
        "rradius",
        "rhand",
        ],
    ee_link_names=["rhand", "rfingers", "rthumb","rpalm"],
    # keypoint_site_names=[
    #     name+"_keyp" for name in ["head_top", "head", "rhumerus", "rradius", "rhand", "lhumerus", "lradius", "lhand"]
    #     ],
    base_joint="human_base_joint",
    ee_site_name="right_hand_site",
    weld_body_name="rpalm",
)
HUMANOID_LEFT_BODY_NAMES=[
    "lclavicle",
    "lhumerus",
    "lradius",
    "lwrist",
    "lhand",
    "lfingers",
    "lthumb",
]
TABLE_GRID_POS = [
    dict(pos=[0.05, 0.3, 0.3], size=[0.08, 0.05, 0.01]),
    dict(pos=[0.05, 0.5, 0.3], size=[0.08, 0.08, 0.01]),
    dict(pos=[0.05, 0.7, 0.3], size=[0.08, 0.05, 0.01]),

    dict(pos=[0.3, 0.3, 0.3], size=[0.08, 0.05, 0.01]),
    dict(pos=[0.3, 0.5, 0.3], size=[0.08, 0.08, 0.01]),
    dict(pos=[0.3, 0.7, 0.3], size=[0.08, 0.05, 0.01]),

    dict(pos=[0.55, 0.3, 0.3], size=[0.08, 0.05, 0.01]),
    dict(pos=[0.55, 0.5, 0.3], size=[0.08, 0.08, 0.01]),
    dict(pos=[0.55, 0.7, 0.3], size=[0.08, 0.05, 0.01]),

    dict(pos=[0.8, 0.3, 0.3], size=[0.08, 0.05, 0.01]),
    dict(pos=[0.8, 0.5, 0.3], size=[0.08, 0.08, 0.01]),
    dict(pos=[0.8, 0.7, 0.3], size=[0.08, 0.05, 0.01]),
]
BIN_GRID_POS = [
    # inside the bin, left side
    dict(pos=[-0.65, 0.68, 0.3], size=[0.1, 0.05, 0.01]),
    dict(pos=[-0.65, 0.5, 0.3], size=[0.1, 0.05, 0.01]),
    dict(pos=[-0.65, 0.32, 0.3], size=[0.1, 0.05, 0.01]),
    # inside the bin, right side
    dict(pos=[-0.38, 0.68, 0.3], size=[0.1, 0.05, 0.01]),
    dict(pos=[-0.38, 0.5, 0.3], size=[0.1, 0.05, 0.01]),
    dict(pos=[-0.38, 0.32, 0.3], size=[0.1, 0.05, 0.01]),
]
BIN_GRID_POS=BIN_GRID_POS[0:1]+BIN_GRID_POS[3:4]
# SCENE_BOUNDS=((-1.5, -0.7, 0.02), (1.5, 2.5, 1.5))
SCENE_BOUNDS=((-1.4, -0.2, -0.1), (1.7, 1.2, 1.1))

HUMAN_KEYPOINT_SITE_NAMES = [name+"_keyp" for \
    name in ["head_top", "head", "rhumerus", "rradius", "rhand", "lhumerus", "lradius", "lhand"]]

 
