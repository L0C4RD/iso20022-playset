from . import base_types
from .Max6AlphaText import Max6AlphaText
from .Exact4NumericText import Exact4NumericText
from .ISODate import ISODate

class AgreementConditions1(base_types._BaseFieldType):

	__slots__ = ["_Vrsn", "_AgrmtCd", "_Dt"]
	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def AgrmtCd(self):
		return self._AgrmtCd

	@AgrmtCd.setter
	def AgrmtCd(self, value):
		self._AgrmtCd = value if type(value) != base_types.auto else self.make_default("AgrmtCd")

	@AgrmtCd.deleter
	def AgrmtCd(self):
		del self._AgrmtCd
		self._AgrmtCd = None

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
		base_types.FieldEntry(name='Vrsn', type=Exact4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrmtCd', type=Max6AlphaText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

