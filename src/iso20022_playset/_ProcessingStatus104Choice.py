# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcknowledgedAcceptedStatus21Choice import AcknowledgedAcceptedStatus21Choice
from ._PendingProcessingStatus22Choice import PendingProcessingStatus22Choice
from ._PendingStatus81Choice import PendingStatus81Choice
from ._ProprietaryReason4 import ProprietaryReason4
from ._ProprietaryStatusAndReason6 import ProprietaryStatusAndReason6
from ._RepairStatus12Choice import RepairStatus12Choice

class ProcessingStatus104Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_CxlReqd", "_PdgCxl", "_PdgPrcg", "_Prtry", "_Rpr"]
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
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

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
		base_types.FieldEntry(name='CxlReqd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingStatus81Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessingStatus22Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rpr', type=RepairStatus12Choice, min=0, max=1, mutex_group=1, array=False),
	))