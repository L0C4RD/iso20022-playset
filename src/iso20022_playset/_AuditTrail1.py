# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max256Text
from . import Max350Text
from . import Max35Text

class AuditTrail1(base_types._BaseFieldType):

	__slots__ = ["_ApprvgUsr", "_FldNm", "_InstgUsr", "_NewFldVal", "_OdFldVal", "_OprTmStmp"]
	@property
	def ApprvgUsr(self):
		return self._ApprvgUsr

	@ApprvgUsr.setter
	def ApprvgUsr(self, value):
		self._ApprvgUsr = value if value is not None else base_types.UninitialisedField(self, 'ApprvgUsr', Max256Text, False)

	@ApprvgUsr.deleter
	def ApprvgUsr(self):
		del self._ApprvgUsr
		self._ApprvgUsr = base_types.UninitialisedField(self, 'ApprvgUsr', Max256Text, False)

	@property
	def FldNm(self):
		return self._FldNm

	@FldNm.setter
	def FldNm(self, value):
		self._FldNm = value if value is not None else base_types.UninitialisedField(self, 'FldNm', Max35Text, False)

	@FldNm.deleter
	def FldNm(self):
		del self._FldNm
		self._FldNm = base_types.UninitialisedField(self, 'FldNm', Max35Text, False)

	@property
	def InstgUsr(self):
		return self._InstgUsr

	@InstgUsr.setter
	def InstgUsr(self, value):
		self._InstgUsr = value if value is not None else base_types.UninitialisedField(self, 'InstgUsr', Max256Text, False)

	@InstgUsr.deleter
	def InstgUsr(self):
		del self._InstgUsr
		self._InstgUsr = base_types.UninitialisedField(self, 'InstgUsr', Max256Text, False)

	@property
	def NewFldVal(self):
		return self._NewFldVal

	@NewFldVal.setter
	def NewFldVal(self, value):
		self._NewFldVal = value if value is not None else base_types.UninitialisedField(self, 'NewFldVal', Max350Text, False)

	@NewFldVal.deleter
	def NewFldVal(self):
		del self._NewFldVal
		self._NewFldVal = base_types.UninitialisedField(self, 'NewFldVal', Max350Text, False)

	@property
	def OdFldVal(self):
		return self._OdFldVal

	@OdFldVal.setter
	def OdFldVal(self, value):
		self._OdFldVal = value if value is not None else base_types.UninitialisedField(self, 'OdFldVal', Max350Text, False)

	@OdFldVal.deleter
	def OdFldVal(self):
		del self._OdFldVal
		self._OdFldVal = base_types.UninitialisedField(self, 'OdFldVal', Max350Text, False)

	@property
	def OprTmStmp(self):
		return self._OprTmStmp

	@OprTmStmp.setter
	def OprTmStmp(self, value):
		self._OprTmStmp = value if value is not None else base_types.UninitialisedField(self, 'OprTmStmp', ISODateTime, False)

	@OprTmStmp.deleter
	def OprTmStmp(self):
		del self._OprTmStmp
		self._OprTmStmp = base_types.UninitialisedField(self, 'OprTmStmp', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApprvgUsr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FldNm', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgUsr', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewFldVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdFldVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))