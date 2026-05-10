import base_types
import ISODateTime
import Max350Text
import Max256Text
import Max35Text

class AuditTrail1(base_types._BaseFieldType):

	__slots__ = ["_OdFldVal", "_OprTmStmp", "_NewFldVal", "_InstgUsr", "_ApprvgUsr", "_FldNm"]
	@property
	def OdFldVal(self):
		return self._OdFldVal

	@OdFldVal.setter
	def OdFldVal(self, value):
		self._OdFldVal = value if type(value) != auto else self.make_default("OdFldVal")

	@OdFldVal.deleter
	def OdFldVal(self):
		del self._OdFldVal
		self._OdFldVal = None

	@property
	def OprTmStmp(self):
		return self._OprTmStmp

	@OprTmStmp.setter
	def OprTmStmp(self, value):
		self._OprTmStmp = value if type(value) != auto else self.make_default("OprTmStmp")

	@OprTmStmp.deleter
	def OprTmStmp(self):
		del self._OprTmStmp
		self._OprTmStmp = None

	@property
	def NewFldVal(self):
		return self._NewFldVal

	@NewFldVal.setter
	def NewFldVal(self, value):
		self._NewFldVal = value if type(value) != auto else self.make_default("NewFldVal")

	@NewFldVal.deleter
	def NewFldVal(self):
		del self._NewFldVal
		self._NewFldVal = None

	@property
	def InstgUsr(self):
		return self._InstgUsr

	@InstgUsr.setter
	def InstgUsr(self, value):
		self._InstgUsr = value if type(value) != auto else self.make_default("InstgUsr")

	@InstgUsr.deleter
	def InstgUsr(self):
		del self._InstgUsr
		self._InstgUsr = None

	@property
	def ApprvgUsr(self):
		return self._ApprvgUsr

	@ApprvgUsr.setter
	def ApprvgUsr(self, value):
		self._ApprvgUsr = value if type(value) != auto else self.make_default("ApprvgUsr")

	@ApprvgUsr.deleter
	def ApprvgUsr(self):
		del self._ApprvgUsr
		self._ApprvgUsr = None

	@property
	def FldNm(self):
		return self._FldNm

	@FldNm.setter
	def FldNm(self, value):
		self._FldNm = value if type(value) != auto else self.make_default("FldNm")

	@FldNm.deleter
	def FldNm(self):
		del self._FldNm
		self._FldNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OdFldVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewFldVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgUsr', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApprvgUsr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FldNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

