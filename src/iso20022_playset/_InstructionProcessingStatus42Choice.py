# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcknowledgedAcceptedStatus21Choice
from . import CancellationStatus24Choice
from . import GeneratedStatus7Choice
from . import PendingProcessingStatus18Choice
from . import PendingStatus38Choice
from . import ProprietaryReason4
from . import RepairStatus12Choice

class InstructionProcessingStatus42Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_Canc", "_CxlReqd", "_Gnrtd", "_ModReqd", "_PdgCxl", "_PdgPrcg", "_Rpr"]
	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if value is not None else base_types.UninitialisedField(self, 'AckdAccptd', AcknowledgedAcceptedStatus21Choice, False)

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = base_types.UninitialisedField(self, 'AckdAccptd', AcknowledgedAcceptedStatus21Choice, False)

	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if value is not None else base_types.UninitialisedField(self, 'Canc', CancellationStatus24Choice, False)

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = base_types.UninitialisedField(self, 'Canc', CancellationStatus24Choice, False)

	@property
	def CxlReqd(self):
		return self._CxlReqd

	@CxlReqd.setter
	def CxlReqd(self, value):
		self._CxlReqd = value if value is not None else base_types.UninitialisedField(self, 'CxlReqd', ProprietaryReason4, False)

	@CxlReqd.deleter
	def CxlReqd(self):
		del self._CxlReqd
		self._CxlReqd = base_types.UninitialisedField(self, 'CxlReqd', ProprietaryReason4, False)

	@property
	def Gnrtd(self):
		return self._Gnrtd

	@Gnrtd.setter
	def Gnrtd(self, value):
		self._Gnrtd = value if value is not None else base_types.UninitialisedField(self, 'Gnrtd', GeneratedStatus7Choice, False)

	@Gnrtd.deleter
	def Gnrtd(self):
		del self._Gnrtd
		self._Gnrtd = base_types.UninitialisedField(self, 'Gnrtd', GeneratedStatus7Choice, False)

	@property
	def ModReqd(self):
		return self._ModReqd

	@ModReqd.setter
	def ModReqd(self, value):
		self._ModReqd = value if value is not None else base_types.UninitialisedField(self, 'ModReqd', ProprietaryReason4, False)

	@ModReqd.deleter
	def ModReqd(self):
		del self._ModReqd
		self._ModReqd = base_types.UninitialisedField(self, 'ModReqd', ProprietaryReason4, False)

	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if value is not None else base_types.UninitialisedField(self, 'PdgCxl', PendingStatus38Choice, False)

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = base_types.UninitialisedField(self, 'PdgCxl', PendingStatus38Choice, False)

	@property
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if value is not None else base_types.UninitialisedField(self, 'PdgPrcg', PendingProcessingStatus18Choice, False)

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = base_types.UninitialisedField(self, 'PdgPrcg', PendingProcessingStatus18Choice, False)

	@property
	def Rpr(self):
		return self._Rpr

	@Rpr.setter
	def Rpr(self, value):
		self._Rpr = value if value is not None else base_types.UninitialisedField(self, 'Rpr', RepairStatus12Choice, False)

	@Rpr.deleter
	def Rpr(self):
		del self._Rpr
		self._Rpr = base_types.UninitialisedField(self, 'Rpr', RepairStatus12Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus21Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancellationStatus24Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlReqd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Gnrtd', type=GeneratedStatus7Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ModReqd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingStatus38Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessingStatus18Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rpr', type=RepairStatus12Choice, min=0, max=1, mutex_group=1, array=False),
	))