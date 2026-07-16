# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcknowledgedAcceptedStatus24Choice
from . import CancellationStatus15Choice
from . import DeniedStatus16Choice
from . import PendingStatus39Choice
from . import ProprietaryStatusAndReason6
from . import RejectionOrRepairStatus39Choice

class ProcessingStatus69Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_Canc", "_Dnd", "_PdgCxl", "_Prtry", "_Rjctd", "_Rpr"]
	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if value is not None else base_types.UninitialisedField(self, 'AckdAccptd', AcknowledgedAcceptedStatus24Choice, False)

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = base_types.UninitialisedField(self, 'AckdAccptd', AcknowledgedAcceptedStatus24Choice, False)

	@property
	def Canc(self):
		return self._Canc

	@Canc.setter
	def Canc(self, value):
		self._Canc = value if value is not None else base_types.UninitialisedField(self, 'Canc', CancellationStatus15Choice, False)

	@Canc.deleter
	def Canc(self):
		del self._Canc
		self._Canc = base_types.UninitialisedField(self, 'Canc', CancellationStatus15Choice, False)

	@property
	def Dnd(self):
		return self._Dnd

	@Dnd.setter
	def Dnd(self, value):
		self._Dnd = value if value is not None else base_types.UninitialisedField(self, 'Dnd', DeniedStatus16Choice, False)

	@Dnd.deleter
	def Dnd(self):
		del self._Dnd
		self._Dnd = base_types.UninitialisedField(self, 'Dnd', DeniedStatus16Choice, False)

	@property
	def PdgCxl(self):
		return self._PdgCxl

	@PdgCxl.setter
	def PdgCxl(self, value):
		self._PdgCxl = value if value is not None else base_types.UninitialisedField(self, 'PdgCxl', PendingStatus39Choice, False)

	@PdgCxl.deleter
	def PdgCxl(self):
		del self._PdgCxl
		self._PdgCxl = base_types.UninitialisedField(self, 'PdgCxl', PendingStatus39Choice, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryStatusAndReason6, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectionOrRepairStatus39Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectionOrRepairStatus39Choice, False)

	@property
	def Rpr(self):
		return self._Rpr

	@Rpr.setter
	def Rpr(self, value):
		self._Rpr = value if value is not None else base_types.UninitialisedField(self, 'Rpr', RejectionOrRepairStatus39Choice, False)

	@Rpr.deleter
	def Rpr(self):
		del self._Rpr
		self._Rpr = base_types.UninitialisedField(self, 'Rpr', RejectionOrRepairStatus39Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus24Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Canc', type=CancellationStatus15Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dnd', type=DeniedStatus16Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgCxl', type=PendingStatus39Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionOrRepairStatus39Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rpr', type=RejectionOrRepairStatus39Choice, min=0, max=1, mutex_group=1, array=False),
	))