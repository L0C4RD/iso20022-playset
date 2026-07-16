# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancelledCompleteReason1
from . import RejectionReason33
from . import TransferCancellationPendingStatus1
from . import TransferCancellationStatus3

class Status31Choice(base_types._BaseFieldType):

	__slots__ = ["_Cmplt", "_Pdg", "_Rjctd", "_Sts"]
	@property
	def Cmplt(self):
		return self._Cmplt

	@Cmplt.setter
	def Cmplt(self, value):
		self._Cmplt = value if value is not None else base_types.UninitialisedField(self, 'Cmplt', CancelledCompleteReason1, False)

	@Cmplt.deleter
	def Cmplt(self):
		del self._Cmplt
		self._Cmplt = base_types.UninitialisedField(self, 'Cmplt', CancelledCompleteReason1, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', TransferCancellationPendingStatus1, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', TransferCancellationPendingStatus1, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectionReason33, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectionReason33, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', TransferCancellationStatus3, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', TransferCancellationStatus3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cmplt', type=CancelledCompleteReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=TransferCancellationPendingStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionReason33, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sts', type=TransferCancellationStatus3, min=0, max=1, mutex_group=1, array=False),
	))