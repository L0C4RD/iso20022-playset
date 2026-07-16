# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcknowledgedAcceptedStatus21Choice
from . import DeniedStatus15Choice
from . import PendingStatus83Choice
from . import ProprietaryReason4
from . import ProprietaryStatusAndReason6
from . import RejectionOrRepairStatus42Choice

class ProcessingStatus106Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_Cmpltd", "_Dnd", "_Pdg", "_Prtry", "_Rjctd"]
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
	def Cmpltd(self):
		return self._Cmpltd

	@Cmpltd.setter
	def Cmpltd(self, value):
		self._Cmpltd = value if value is not None else base_types.UninitialisedField(self, 'Cmpltd', ProprietaryReason4, False)

	@Cmpltd.deleter
	def Cmpltd(self):
		del self._Cmpltd
		self._Cmpltd = base_types.UninitialisedField(self, 'Cmpltd', ProprietaryReason4, False)

	@property
	def Dnd(self):
		return self._Dnd

	@Dnd.setter
	def Dnd(self, value):
		self._Dnd = value if value is not None else base_types.UninitialisedField(self, 'Dnd', DeniedStatus15Choice, False)

	@Dnd.deleter
	def Dnd(self):
		del self._Dnd
		self._Dnd = base_types.UninitialisedField(self, 'Dnd', DeniedStatus15Choice, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus83Choice, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus83Choice, False)

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
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectionOrRepairStatus42Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectionOrRepairStatus42Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus21Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmpltd', type=ProprietaryReason4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dnd', type=DeniedStatus15Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus83Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionOrRepairStatus42Choice, min=0, max=1, mutex_group=1, array=False),
	))