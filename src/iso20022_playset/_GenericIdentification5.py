from . import base_types
from ._Exact4AlphaNumericText import Exact4AlphaNumericText
from ._Max35Text import Max35Text
from ._Max8Text import Max8Text

class GenericIdentification5(base_types._BaseFieldType):

	__slots__ = ["_Inf", "_Issr", "_Nrrtv"]
	@property
	def Inf(self):
		return self._Inf

	@Inf.setter
	def Inf(self, value):
		self._Inf = value if type(value) != base_types.auto else self.make_default("Inf")

	@Inf.deleter
	def Inf(self):
		del self._Inf
		self._Inf = None

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
	def Nrrtv(self):
		return self._Nrrtv

	@Nrrtv.setter
	def Nrrtv(self, value):
		self._Nrrtv = value if type(value) != base_types.auto else self.make_default("Nrrtv")

	@Nrrtv.deleter
	def Nrrtv(self):
		del self._Nrrtv
		self._Nrrtv = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Inf', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max8Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nrrtv', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

