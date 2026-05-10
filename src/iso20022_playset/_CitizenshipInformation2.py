from . import base_types
from ._YesNoIndicator import YesNoIndicator
from ._NationalityCode import NationalityCode

class CitizenshipInformation2(base_types._BaseFieldType):

	__slots__ = ["_Ntlty", "_MnrInd"]
	@property
	def Ntlty(self):
		return self._Ntlty

	@Ntlty.setter
	def Ntlty(self, value):
		self._Ntlty = value if type(value) != base_types.auto else self.make_default("Ntlty")

	@Ntlty.deleter
	def Ntlty(self):
		del self._Ntlty
		self._Ntlty = None

	@property
	def MnrInd(self):
		return self._MnrInd

	@MnrInd.setter
	def MnrInd(self, value):
		self._MnrInd = value if type(value) != base_types.auto else self.make_default("MnrInd")

	@MnrInd.deleter
	def MnrInd(self):
		del self._MnrInd
		self._MnrInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ntlty', type=NationalityCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

