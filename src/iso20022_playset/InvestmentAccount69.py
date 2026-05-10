from . import base_types
import PartyIdentification132
import Max35Text

class InvestmentAccount69(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Svcr", "_AcctNm", "_Dsgnt"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Svcr(self):
		return self._Svcr

	@Svcr.setter
	def Svcr(self, value):
		self._Svcr = value if type(value) != auto else self.make_default("Svcr")

	@Svcr.deleter
	def Svcr(self):
		del self._Svcr
		self._Svcr = None

	@property
	def AcctNm(self):
		return self._AcctNm

	@AcctNm.setter
	def AcctNm(self, value):
		self._AcctNm = value if type(value) != auto else self.make_default("AcctNm")

	@AcctNm.deleter
	def AcctNm(self):
		del self._AcctNm
		self._AcctNm = None

	@property
	def Dsgnt(self):
		return self._Dsgnt

	@Dsgnt.setter
	def Dsgnt(self, value):
		self._Dsgnt = value if type(value) != auto else self.make_default("Dsgnt")

	@Dsgnt.deleter
	def Dsgnt(self):
		del self._Dsgnt
		self._Dsgnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Svcr', type=PartyIdentification132, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dsgnt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

