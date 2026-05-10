from . import base_types
from .AdjustmentRequest1 import AdjustmentRequest1
from .Max500Text import Max500Text
from .CompensationRequest1 import CompensationRequest1
from .DebitAuthorisation3 import DebitAuthorisation3

class AdditionalRequestData1Choice(base_types._BaseFieldType):

	__slots__ = ["_ReqdDbtAuthstn", "_ReqdValtn", "_ReqdCompstn", "_ReqNrrtv"]
	@property
	def ReqdDbtAuthstn(self):
		return self._ReqdDbtAuthstn

	@ReqdDbtAuthstn.setter
	def ReqdDbtAuthstn(self, value):
		self._ReqdDbtAuthstn = value if type(value) != auto else self.make_default("ReqdDbtAuthstn")

	@ReqdDbtAuthstn.deleter
	def ReqdDbtAuthstn(self):
		del self._ReqdDbtAuthstn
		self._ReqdDbtAuthstn = None

	@property
	def ReqdValtn(self):
		return self._ReqdValtn

	@ReqdValtn.setter
	def ReqdValtn(self, value):
		self._ReqdValtn = value if type(value) != auto else self.make_default("ReqdValtn")

	@ReqdValtn.deleter
	def ReqdValtn(self):
		del self._ReqdValtn
		self._ReqdValtn = None

	@property
	def ReqdCompstn(self):
		return self._ReqdCompstn

	@ReqdCompstn.setter
	def ReqdCompstn(self, value):
		self._ReqdCompstn = value if type(value) != auto else self.make_default("ReqdCompstn")

	@ReqdCompstn.deleter
	def ReqdCompstn(self):
		del self._ReqdCompstn
		self._ReqdCompstn = None

	@property
	def ReqNrrtv(self):
		return self._ReqNrrtv

	@ReqNrrtv.setter
	def ReqNrrtv(self, value):
		self._ReqNrrtv = value if type(value) != auto else self.make_default("ReqNrrtv")

	@ReqNrrtv.deleter
	def ReqNrrtv(self):
		del self._ReqNrrtv
		self._ReqNrrtv = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqdDbtAuthstn', type=DebitAuthorisation3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ReqdValtn', type=AdjustmentRequest1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ReqdCompstn', type=CompensationRequest1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ReqNrrtv', type=Max500Text, min=0, max=1, mutex_group=1, array=False),
	))

