# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ProprietaryReason5
from . import ProprietaryStatusAndReason7
from . import UnmatchedStatus19Choice

class MatchingStatus29Choice(base_types._BaseFieldType):

	__slots__ = ["_Mtchd", "_Prtry", "_Umtchd"]
	@property
	def Mtchd(self):
		return self._Mtchd

	@Mtchd.setter
	def Mtchd(self, value):
		self._Mtchd = value if value is not None else base_types.UninitialisedField(self, 'Mtchd', ProprietaryReason5, False)

	@Mtchd.deleter
	def Mtchd(self):
		del self._Mtchd
		self._Mtchd = base_types.UninitialisedField(self, 'Mtchd', ProprietaryReason5, False)

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
	def Umtchd(self):
		return self._Umtchd

	@Umtchd.setter
	def Umtchd(self, value):
		self._Umtchd = value if value is not None else base_types.UninitialisedField(self, 'Umtchd', UnmatchedStatus19Choice, False)

	@Umtchd.deleter
	def Umtchd(self):
		del self._Umtchd
		self._Umtchd = base_types.UninitialisedField(self, 'Umtchd', UnmatchedStatus19Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mtchd', type=ProprietaryReason5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryStatusAndReason7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Umtchd', type=UnmatchedStatus19Choice, min=0, max=1, mutex_group=1, array=False),
	))