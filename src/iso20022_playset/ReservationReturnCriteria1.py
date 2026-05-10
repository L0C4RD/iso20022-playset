import base_types
import RequestedIndicator

class ReservationReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_StsInd", "_StartDtTmInd"]
	@property
	def StsInd(self):
		return self._StsInd

	@StsInd.setter
	def StsInd(self, value):
		self._StsInd = value if type(value) != auto else self.make_default("StsInd")

	@StsInd.deleter
	def StsInd(self):
		del self._StsInd
		self._StsInd = None

	@property
	def StartDtTmInd(self):
		return self._StartDtTmInd

	@StartDtTmInd.setter
	def StartDtTmInd(self, value):
		self._StartDtTmInd = value if type(value) != auto else self.make_default("StartDtTmInd")

	@StartDtTmInd.deleter
	def StartDtTmInd(self):
		del self._StartDtTmInd
		self._StartDtTmInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDtTmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

