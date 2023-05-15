from omni.isaac.orbit.actuators.group import ActuatorGroupCfg
from omni.isaac.orbit.actuators.group.actuator_group_cfg import ActuatorControlCfg
from omni.isaac.orbit.actuators.model import ImplicitActuatorCfg
from omni.isaac.orbit.robots.single_arm import SingleArmManipulatorCfg
from omni.isaac.orbit.robots.mobile_manipulator import MobileManipulator
from omni.isaac.orbit.robots.mobile_manipulator import MobileManipulatorCfg

PEPPER_USD_PATH="/home/cjf/Desktop/Isaac/orbit/Orbit/Asset/pepper_description/urdf/pepper/pepper_simple.usd"

PEPPER_CFG_simple = MobileManipulatorCfg(
    meta_info=MobileManipulatorCfg.MetaInfoCfg(
        usd_path=PEPPER_USD_PATH,
	base_num_dof=3,
	arm_num_dof=3,
    ),
    init_state=MobileManipulatorCfg.InitialStateCfg(
        dof_pos={
            # pepper base
	   "XDisp": 0.0,
	   "YDisp": 0.0,
	   "ZRot": 0.0,
	   #Pepper arm
	   "KneePitch": 0.0,
	   "HipPitch": 0.0,
	   #Pepper tool
	   "endeffectorJ": 0.0,
        },
        dof_vel={".*": 0.0},
    ),
    ee_info=MobileManipulatorCfg.EndEffectorFrameCfg(
        body_name="endeffector", pos_offset=(0.0, 0.0, 0.602), rot_offset=(1.0, 0.0, 0.0, 0.0)
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
            dof_names=["XDisp",
		       "YDisp",
		       "ZRot",
		      ],
            model_cfg=ImplicitActuatorCfg(velocity_limit=100.0, torque_limit=1000.0),
            control_cfg=ActuatorControlCfg(
                command_types=["v_abs"],
                stiffness={".*": 800.0},
                damping={".*": 40.0},
                dof_pos_offset={
                    #"BWheelYaw": 0.0,
                    #"BWheelPitch": 0.0,
                    #"FLWheelYaw": 0.0,
		    #"FLWheelPitch": 0.0,
		    #"FRWheelYaw": 0.0,
		    #"FRWheelPitch": 0.0
                },
            ),
        ),
        "pepper_body": ActuatorGroupCfg(
            dof_names=["KneePitch",
		       "HipPitch",
		       "endeffectorJ",
		      ],
            model_cfg=ImplicitActuatorCfg(velocity_limit=100.0, torque_limit=54.0),
            control_cfg=ActuatorControlCfg(
                command_types=["p_abs"],
                stiffness={".*": 800.0},
                damping={".*": 40.0},
                dof_pos_offset={"KneePitch": 0.0,
				"HipPitch": 0.0,
		       		"endeffectorJ": 0.0,
		},
            ),
        ),
    },
)
