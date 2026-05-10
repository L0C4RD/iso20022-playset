import base_types
import Max35Text
import DistributionRejectionStatus1
import MovementProcessingStatus1

class IndividualMovementStatus1(base_types._BaseFieldType):

	__slots__ = ["_MvmntId", "_RjctdSts", "_PrcdSts"]
	@property
	def MvmntId(self):
		return self._MvmntId

	@MvmntId.setter
	def MvmntId(self, value):
		self._MvmntId = value if type(value) != auto else self.make_default("MvmntId")

	@MvmntId.deleter
	def MvmntId(self):
		del self._MvmntId
		self._MvmntId = None

	@property
	def RjctdSts(self):
		return self._RjctdSts

	@RjctdSts.setter
	def RjctdSts(self, value):
		self._RjctdSts = value if type(value) != auto else self.make_default("RjctdSts")

	@RjctdSts.deleter
	def RjctdSts(self):
		del self._RjctdSts
		self._RjctdSts = None

	@property
	def PrcdSts(self):
		return self._PrcdSts

	@PrcdSts.setter
	def PrcdSts(self, value):
		self._PrcdSts = value if type(value) != auto else self.make_default("PrcdSts")

	@PrcdSts.deleter
	def PrcdSts(self):
		del self._PrcdSts
		self._PrcdSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdSts', type=DistributionRejectionStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrcdSts', type=MovementProcessingStatus1, min=0, max=1, mutex_group=1, array=False),
	))

