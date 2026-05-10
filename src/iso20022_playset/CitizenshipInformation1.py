import base_types
import NationalityCode
import ISODate
import YesNoIndicator

class CitizenshipInformation1(base_types._BaseFieldType):

	__slots__ = ["_StartDt", "_MnrInd", "_Ntlty", "_EndDt"]
	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

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

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if type(value) != auto else self.make_default("EndDt")

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntlty', type=NationalityCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

