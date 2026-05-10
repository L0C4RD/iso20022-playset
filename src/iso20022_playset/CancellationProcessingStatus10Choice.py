from . import base_types
from .CancellationReason39Choice import CancellationReason39Choice
from .ProprietaryStatusAndReason6 import ProprietaryStatusAndReason6
from .ProprietaryReason4 import ProprietaryReason4

class CancellationProcessingStatus10Choice(base_types._BaseFieldType):

	__slots__ = ["_CxlCmpltd", "_CxlReqd", "_PrtrySts", "_CxlPdg"]
	@property
	def CxlCmpltd(self):
		return self._CxlCmpltd

	@CxlCmpltd.setter
	def CxlCmpltd(self, value):
		self._CxlCmpltd = value if type(value) != auto else self.make_default("CxlCmpltd")

	@CxlCmpltd.deleter
	def CxlCmpltd(self):
		del self._CxlCmpltd
		self._CxlCmpltd = None

	@property
	def CxlReqd(self):
		return self._CxlReqd

	@CxlReqd.setter
	def CxlReqd(self, value):
		self._CxlReqd = value if type(value) != auto else self.make_default("CxlReqd")

	@CxlReqd.deleter
	def CxlReqd(self):
		del self._CxlReqd
		self._CxlReqd = None

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if type(value) != auto else self.make_default("PrtrySts")

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = None

	@property
	def CxlPdg(self):
		return self._CxlPdg

	@CxlPdg.setter
	def CxlPdg(self, value):
		self._CxlPdg = value if type(value) != auto else self.make_default("CxlPdg")

	@CxlPdg.deleter
	def CxlPdg(self):
		del self._CxlPdg
		self._CxlPdg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlCmpltd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlReqd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlPdg', type=CancellationReason39Choice, min=0, max=1, mutex_group=1, array=False),
	))

