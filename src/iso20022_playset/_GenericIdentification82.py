from . import base_types
from .Max35Text import Max35Text
from .ISODate import ISODate
from .CountryCode import CountryCode
from .OtherIdentification3Choice import OtherIdentification3Choice
from .Max70Text import Max70Text

class GenericIdentification82(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Tp", "_Stat", "_IssrCtry", "_Issr", "_XpryDt", "_IsseDt"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Stat(self):
		return self._Stat

	@Stat.setter
	def Stat(self, value):
		self._Stat = value if type(value) != base_types.auto else self.make_default("Stat")

	@Stat.deleter
	def Stat(self):
		del self._Stat
		self._Stat = None

	@property
	def IssrCtry(self):
		return self._IssrCtry

	@IssrCtry.setter
	def IssrCtry(self, value):
		self._IssrCtry = value if type(value) != base_types.auto else self.make_default("IssrCtry")

	@IssrCtry.deleter
	def IssrCtry(self):
		del self._IssrCtry
		self._IssrCtry = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != base_types.auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=OtherIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Stat', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

