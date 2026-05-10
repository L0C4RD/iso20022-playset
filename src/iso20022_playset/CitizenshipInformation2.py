import base_types
import NationalityCode
import YesNoIndicator

class CitizenshipInformation2(base_types._BaseFieldType):

	__slots__ = ["_MnrInd", "_Ntlty"]
	@property
	def MnrInd(self):
		return self._MnrInd

	@MnrInd.setter
	def MnrInd(self, value):
		self._MnrInd = value if type(value) != auto else self.make_default("MnrInd")

	@MnrInd.deleter
	def MnrInd(self):
		del self._MnrInd
		self._MnrInd = None

	@property
	def Ntlty(self):
		return self._Ntlty

	@Ntlty.setter
	def Ntlty(self, value):
		self._Ntlty = value if type(value) != auto else self.make_default("Ntlty")

	@Ntlty.deleter
	def Ntlty(self):
		del self._Ntlty
		self._Ntlty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MnrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntlty', type=NationalityCode, min=1, max=1, mutex_group=None, array=False),
	))

