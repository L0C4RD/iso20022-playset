# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcknowledgedAcceptedStatus25Choice
from . import PendingProcessingStatus15Choice
from . import PendingStatus46Choice
from . import ProprietaryReason5
from . import ProprietaryStatusAndReason7
from . import RepairStatus16Choice

class ProcessingStatus62Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_CxlReqd", "_PdgCxl", "_PdgPrcg", "_Prtry", "_Rpr"]
	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if value is not None else base_types.UninitialisedField(self, 'AckdAccptd', AcknowledgedAcceptedStatus25Choice, False)

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = base_types.UninitialisedField(self, 'AckdAccptd', AcknowledgedAcceptedStatus25Choice, False)

	@property
	def CxlReqd(self):
		return self._CxlReqd

	@CxlReqd.setter
	def CxlReqd(self, value):
		self._CxlReqd = value if value is not None else base_types.UninitialisedField(self, 'CxlReqd', ProprietaryReason5, False)

	@CxlReqd.deleter
	def CxlReqd(self):
		del self._CxlReqd
		self._CxlReqd = base_types.UninitialisedField(self, 'CxlReqd', ProprietaryReason5, False)

	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if value is not None else base_types.UninitialisedField(self, 'PdgCxl', PendingStatus46Choice, False)

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = base_types.UninitialisedField(self, 'PdgCxl', PendingStatus46Choice, False)

	@property
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if value is not None else base_types.UninitialisedField(self, 'PdgPrcg', PendingProcessingStatus15Choice, False)

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = base_types.UninitialisedField(self, 'PdgPrcg', PendingProcessingStatus15Choice, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason7, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason7, False)

	@property
	def Rpr(self):
		return self._Rpr

	@Rpr.setter
	def Rpr(self, value):
		self._Rpr = value if value is not None else base_types.UninitialisedField(self, 'Rpr', RepairStatus16Choice, False)

	@Rpr.deleter
	def Rpr(self):
		del self._Rpr
		self._Rpr = base_types.UninitialisedField(self, 'Rpr', RepairStatus16Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus25Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlReqd', type=ProprietaryReason5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingStatus46Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessingStatus15Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rpr', type=RepairStatus16Choice, min=0, max=1, mutex_group=1, array=False),
	))