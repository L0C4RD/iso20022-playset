from . import base_types
from .AuthenticationChannel1Choice import AuthenticationChannel1Choice
from .Max16Text import Max16Text
from .ISODate import ISODate

class MandateAuthentication1(base_types._BaseFieldType):

	__slots__ = ["_MsgAuthntcnCd", "_Chanl", "_Dt"]
	@property
	def MsgAuthntcnCd(self):
		return self._MsgAuthntcnCd

	@MsgAuthntcnCd.setter
	def MsgAuthntcnCd(self, value):
		self._MsgAuthntcnCd = value if type(value) != base_types.auto else self.make_default("MsgAuthntcnCd")

	@MsgAuthntcnCd.deleter
	def MsgAuthntcnCd(self):
		del self._MsgAuthntcnCd
		self._MsgAuthntcnCd = None

	@property
	def Chanl(self):
		return self._Chanl

	@Chanl.setter
	def Chanl(self, value):
		self._Chanl = value if type(value) != base_types.auto else self.make_default("Chanl")

	@Chanl.deleter
	def Chanl(self):
		del self._Chanl
		self._Chanl = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgAuthntcnCd', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chanl', type=AuthenticationChannel1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

