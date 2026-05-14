# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcknowledgedAcceptedStatus21Choice import AcknowledgedAcceptedStatus21Choice
from ._CancellationStatus24Choice import CancellationStatus24Choice
from ._GeneratedStatus7Choice import GeneratedStatus7Choice
from ._PendingProcessingStatus20Choice import PendingProcessingStatus20Choice
from ._PendingStatus81Choice import PendingStatus81Choice
from ._ProprietaryReason4 import ProprietaryReason4
from ._RepairStatus12Choice import RepairStatus12Choice

class InstructionProcessingStatus63Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_Canc", "_CxlReqd", "_Gnrtd", "_ModReqd", "_PdgCxl", "_PdgPrcg", "_Rpr"]
	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if type(value) != base_types.auto else self.make_default("AckdAccptd")

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = None

	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if type(value) != base_types.auto else self.make_default("Canc")

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = None

	@property
	def CxlReqd(self):
		return self._CxlReqd

	@CxlReqd.setter
	def CxlReqd(self, value):
		self._CxlReqd = value if type(value) != base_types.auto else self.make_default("CxlReqd")

	@CxlReqd.deleter
	def CxlReqd(self):
		del self._CxlReqd
		self._CxlReqd = None

	@property
	def Gnrtd(self):
		return self._Gnrtd

	@Gnrtd.setter
	def Gnrtd(self, value):
		self._Gnrtd = value if type(value) != base_types.auto else self.make_default("Gnrtd")

	@Gnrtd.deleter
	def Gnrtd(self):
		del self._Gnrtd
		self._Gnrtd = None

	@property
	def ModReqd(self):
		return self._ModReqd

	@ModReqd.setter
	def ModReqd(self, value):
		self._ModReqd = value if type(value) != base_types.auto else self.make_default("ModReqd")

	@ModReqd.deleter
	def ModReqd(self):
		del self._ModReqd
		self._ModReqd = None

	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if type(value) != base_types.auto else self.make_default("PdgCxl")

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = None

	@property
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if type(value) != base_types.auto else self.make_default("PdgPrcg")

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = None

	@property
	def Rpr(self):
		return self._Rpr

	@Rpr.setter
	def Rpr(self, value):
		self._Rpr = value if type(value) != base_types.auto else self.make_default("Rpr")

	@Rpr.deleter
	def Rpr(self):
		del self._Rpr
		self._Rpr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus21Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancellationStatus24Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlReqd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Gnrtd', type=GeneratedStatus7Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ModReqd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingStatus81Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessingStatus20Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rpr', type=RepairStatus12Choice, min=0, max=1, mutex_group=1, array=False),
	))