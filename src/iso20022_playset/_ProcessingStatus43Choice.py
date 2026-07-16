# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptedStatusReason7
from . import PendingProcessingStatusReason1
from . import ProprietaryStatusAndReason5
from . import ReceivedStatusReason1
from . import RejectedStatusReason12

class ProcessingStatus43Choice(base_types._BaseFieldType):

	__slots__ = ["_Accptd", "_PdgPrcg", "_PrtrySts", "_Rcvd", "_Rjctd"]
	@property
	def Accptd(self):
		return self._Accptd

	@Accptd.setter
	def Accptd(self, value):
		self._Accptd = value if value is not None else base_types.UninitialisedField(self, 'Accptd', AcceptedStatusReason7, False)

	@Accptd.deleter
	def Accptd(self):
		del self._Accptd
		self._Accptd = base_types.UninitialisedField(self, 'Accptd', AcceptedStatusReason7, False)

	@property
	def PdgPrcg(self):
		return self._PdgPrcg

	@PdgPrcg.setter
	def PdgPrcg(self, value):
		self._PdgPrcg = value if value is not None else base_types.UninitialisedField(self, 'PdgPrcg', PendingProcessingStatusReason1, False)

	@PdgPrcg.deleter
	def PdgPrcg(self):
		del self._PdgPrcg
		self._PdgPrcg = base_types.UninitialisedField(self, 'PdgPrcg', PendingProcessingStatusReason1, False)

	@property
	def PrtrySts(self):
		return self._PrtrySts

	@PrtrySts.setter
	def PrtrySts(self, value):
		self._PrtrySts = value if value is not None else base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason5, False)

	@PrtrySts.deleter
	def PrtrySts(self):
		del self._PrtrySts
		self._PrtrySts = base_types.UninitialisedField(self, 'PrtrySts', ProprietaryStatusAndReason5, False)

	@property
	def Rcvd(self):
		return self._Rcvd

	@Rcvd.setter
	def Rcvd(self, value):
		self._Rcvd = value if value is not None else base_types.UninitialisedField(self, 'Rcvd', ReceivedStatusReason1, False)

	@Rcvd.deleter
	def Rcvd(self):
		del self._Rcvd
		self._Rcvd = base_types.UninitialisedField(self, 'Rcvd', ReceivedStatusReason1, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectedStatusReason12, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectedStatusReason12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Accptd', type=AcceptedStatusReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPrcg', type=PendingProcessingStatusReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtrySts', type=ProprietaryStatusAndReason5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rcvd', type=ReceivedStatusReason1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectedStatusReason12, min=0, max=1, mutex_group=1, array=False),
	))