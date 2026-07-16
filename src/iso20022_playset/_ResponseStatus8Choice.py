# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ConsentStatus5Choice
from . import PendingStatus20Choice
from . import RejectionStatus27Choice

class ResponseStatus8Choice(base_types._BaseFieldType):

	__slots__ = ["_Cnsntd", "_Pdg", "_Rjctd"]
	@property
	def Cnsntd(self):
		return self._Cnsntd

	@Cnsntd.setter
	def Cnsntd(self, value):
		self._Cnsntd = value if value is not None else base_types.UninitialisedField(self, 'Cnsntd', ConsentStatus5Choice, False)

	@Cnsntd.deleter
	def Cnsntd(self):
		del self._Cnsntd
		self._Cnsntd = base_types.UninitialisedField(self, 'Cnsntd', ConsentStatus5Choice, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus20Choice, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus20Choice, False)

	@property
	def Rjctd(self):
		return self._Rjctd

	@Rjctd.setter
	def Rjctd(self, value):
		self._Rjctd = value if value is not None else base_types.UninitialisedField(self, 'Rjctd', RejectionStatus27Choice, False)

	@Rjctd.deleter
	def Rjctd(self):
		del self._Rjctd
		self._Rjctd = base_types.UninitialisedField(self, 'Rjctd', RejectionStatus27Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cnsntd', type=ConsentStatus5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus20Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rjctd', type=RejectionStatus27Choice, min=0, max=1, mutex_group=1, array=False),
	))