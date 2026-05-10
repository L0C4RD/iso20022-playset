from . import base_types
from .Number import Number
from .ActiveCurrencyCode import ActiveCurrencyCode
from .Exact3NumericText import Exact3NumericText
from .Max35Text import Max35Text

class CurrencyDetails3(base_types._BaseFieldType):

	__slots__ = ["_NmrcCd", "_Dcml", "_AlphaCd", "_Nm"]
	@property
	def NmrcCd(self):
		return self._NmrcCd

	@NmrcCd.setter
	def NmrcCd(self, value):
		self._NmrcCd = value if type(value) != base_types.auto else self.make_default("NmrcCd")

	@NmrcCd.deleter
	def NmrcCd(self):
		del self._NmrcCd
		self._NmrcCd = None

	@property
	def Dcml(self):
		return self._Dcml

	@Dcml.setter
	def Dcml(self, value):
		self._Dcml = value if type(value) != base_types.auto else self.make_default("Dcml")

	@Dcml.deleter
	def Dcml(self):
		del self._Dcml
		self._Dcml = None

	@property
	def AlphaCd(self):
		return self._AlphaCd

	@AlphaCd.setter
	def AlphaCd(self, value):
		self._AlphaCd = value if type(value) != base_types.auto else self.make_default("AlphaCd")

	@AlphaCd.deleter
	def AlphaCd(self):
		del self._AlphaCd
		self._AlphaCd = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NmrcCd', type=Exact3NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dcml', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AlphaCd', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

