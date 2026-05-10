from . import base_types
import UpdateLogPartyRecord2Choice
import Max256Text
import ISODateTime

class PartyAuditTrail2(base_types._BaseFieldType):

	__slots__ = ["_ApprvgUsr", "_Rcrd", "_InstgUsr", "_OprTmStmp"]
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
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if type(value) != auto else self.make_default("Rcrd")

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = None

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
	def OprTmStmp(self):
		return self._OprTmStmp

	@OprTmStmp.setter
	def OprTmStmp(self, value):
		self._OprTmStmp = value if type(value) != auto else self.make_default("OprTmStmp")

	@OprTmStmp.deleter
	def OprTmStmp(self):
		del self._OprTmStmp
		self._OprTmStmp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApprvgUsr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=UpdateLogPartyRecord2Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstgUsr', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprTmStmp', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

