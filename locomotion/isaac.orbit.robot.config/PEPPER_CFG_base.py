from omni.isaac.orbit.actuators.group import ActuatorGroupCfg
from omni.isaac.orbit.actuators.group.actuator_group_cfg import ActuatorControlCfg
from omni.isaac.orbit.actuators.model import ImplicitActuatorCfg
from omni.isaac.orbit.robots.single_arm import SingleArmManipulatorCfg
from omni.isaac.orbit.robots.mobile_manipulator import MobileManipulator
from omni.isaac.orbit.robots.mobile_manipulator import MobileManipulatorCfg

PEPPER_USD_PATH="/home/cjf/Desktop/Isaac/orbit/Orbit/Asset/pepper_description/urdf/pepper/pepper_base.usd"

PEPPER_CFG_base = MobileManipulatorCfg(
    meta_info=MobileManipulatorCfg.MetaInfoCfg(
        usd_path=PEPPER_USD_PATH,
	base_num_dof=6,
	arm_num_dof=1,
	#tool_num_dof=1,
    ),
    init_state=MobileManipulatorCfg.InitialStateCfg(
        dof_pos={
           # pepper base
	   "BWheel_Yaw": 0.0,
	   "BWheel_Pitch": 0.0,
	   "FLWheel_Yaw": 0.0,
	   "FLWheel_Pitch": 0.0,
	   "FRWheel_Yaw": 0.0,
	   "FRWheel_Pitch": 0.0,
	   #Pepper arm
	   "KneePitch": 0.0,
	   #Pepper tool
	   "HipRoll": 0.0,
        },
        dof_vel={".*": 0.0},
    ),
    ee_info=MobileManipulatorCfg.EndEffectorFrameCfg(
        body_name="Pelvis", pos_offset=(-0.038, 0.0, 0.9899), rot_offset=(1.0, 0.0, 0.0, 0.0)
    ),
    rigid_props=SingleArmManipulatorCfg.RigidBodyPropertiesCfg(
        max_depenetration_velocity=5.0,
    ),
    collision_props=SingleArmManipulatorCfg.CollisionPropertiesCfg(
        contact_offset=0.005,
        rest_offset=0.0,
    ),
    articulation_props=SingleArmManipulatorCfg.ArticulationRootPropertiesCfg(
        enable_self_collisions=True,
    ),
    actuator_groups={
        "pepper_base": ActuatorGroupCfg(
            dof_names=["BWheel_Yaw",
		       "BWheel_Pitch",
		       "FLWheel_Yaw",
		       "FLWheel_Pitch",
		       "FRWheel_Yaw",
		       "FRWheel_Pitch"
		      ],
            model_cfg=ImplicitActuatorCfg(velocity_limit=100.0, torque_limit=87.0),
            control_cfg=ActuatorControlCfg(
                command_types=["v_abs"],
                stiffness={".*": 800.0},
                damping={".*": 40.0},
                dof_pos_offset={
                    "BWheel_Yaw": 0.0,
                    "BWheel_Pitch": 0.0,
                    "FLWheel_Yaw": 0.0,
		    "FLWheel_Pitch": 0.0,
		    "FRWheel_Yaw": 0.0,
		    "FRWheel_Pitch": 0.0
                },
            ),
        ),
        "pepper_body": ActuatorGroupCfg(
            dof_names=["KneePitch",
		       #"HipRoll"
		      ],
            model_cfg=ImplicitActuatorCfg(velocity_limit=100.0, torque_limit=54.0),
            control_cfg=ActuatorControlCfg(
                command_types=["p_abs"],
                stiffness={".*": 800.0},
                damping={".*": 40.0},
                dof_pos_offset={"KneePitch": 0.0,
				#"HipRoll": 0.0
		},
            ),
        ),
    },
)
