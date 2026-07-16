# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcknowledgedAcceptedStatus30Choice
from . import DeniedStatus19Choice
from . import ModificationStatus5Choice
from . import PendingProcessingStatus16Choice
from . import ProprietaryStatusAndReason7
from . import RejectionStatus42Choice
from . import RepairStatus17Choice

class ModificationProcessingStatus11Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_Dnd", "_Modfd", "_PdgPrcg", "_Prtry", "_Rjctd", "_Rprd"]
	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if value is not None else base_types.UninitialisedField(self, 'AckdAccptd', AcknowledgedAcceptedStatus30Choice, False)

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = base_types.UninitialisedField(self, 'AckdAccptd', AcknowledgedAcceptedStatus30Choice, False)

	@property
	def Dnd(self):
		return self._Dnd

	@Dnd.setter
	def Dnd(self, value):
		self._Dnd = value if value is not None else base_types.UninitialisedField(self, 'Dnd', DeniedStatus19Choice, False)

	@Dnd.deleter
	def Dnd(self):
		del self._Dnd
		self._Dnd = base_types.UninitialisedField(self, 'Dnd', DeniedStatus19Choice, False)

	@property
	def Modfd(self):
		return self._Modfd

	@Modfd.setter
	def Modfd(self, value):
		self._Modfd = value if value is not None else base_types.UninitialisedField(self, 'Modfd', ModificationStatus5Choice, False)

	@Modfd.deleter
	def Modfd(self):
		del self._Modfd
		self._Modfd = base_types.UninitialisedField(self, 'Modfd', ModificationStatus5Choice, False)

	@property
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if value is not None else base_types.UninitialisedField(self, 'PdgPrcg', PendingProcessingStatus16Choice, False)

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = base_types.UninitialisedField(self, 'PdgPrcg', PendingProcessingStatus16Choice, False)

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
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectionStatus42Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectionStatus42Choice, False)

	@property
	def Rprd(self):
		return self._Rprd

	@Rprd.setter
	def Rprd(self, value):
		self._Rprd = value if value is not None else base_types.UninitialisedField(self, 'Rprd', RepairStatus17Choice, False)

	@Rprd.deleter
	def Rprd(self):
		del self._Rprd
		self._Rprd = base_types.UninitialisedField(self, 'Rprd', RepairStatus17Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus30Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dnd', type=DeniedStatus19Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Modfd', type=ModificationStatus5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessingStatus16Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionStatus42Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rprd', type=RepairStatus17Choice, min=0, max=1, mutex_group=1, array=False),
	))