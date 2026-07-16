# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcknowledgedAcceptedStatus22Choice
from . import DeniedStatus17Choice
from . import ProprietaryStatusAndReason6

class RepoCallRequestStatus7Choice(base_types._BaseFieldType):

	__slots__ = ["_AckdAccptd", "_Dnd", "_Prtry"]
	@property
	def AckdAccptd(self):
		return self._AckdAccptd

	@AckdAccptd.setter
	def AckdAccptd(self, value):
		self._AckdAccptd = value if value is not None else base_types.UninitialisedField(self, 'AckdAccptd', AcknowledgedAcceptedStatus22Choice, False)

	@AckdAccptd.deleter
	def AckdAccptd(self):
		del self._AckdAccptd
		self._AckdAccptd = base_types.UninitialisedField(self, 'AckdAccptd', AcknowledgedAcceptedStatus22Choice, False)

	@property
	def Dnd(self):
		return self._Dnd

	@Dnd.setter
	def Dnd(self, value):
		self._Dnd = value if value is not None else base_types.UninitialisedField(self, 'Dnd', DeniedStatus17Choice, False)

	@Dnd.deleter
	def Dnd(self):
		del self._Dnd
		self._Dnd = base_types.UninitialisedField(self, 'Dnd', DeniedStatus17Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckdAccptd', type=AcknowledgedAcceptedStatus22Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dnd', type=DeniedStatus17Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason6, min=0, max=1, mutex_group=1, array=False),
	))