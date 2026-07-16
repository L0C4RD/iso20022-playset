# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import YesNoIndicator

class ReconciliationCategory4(base_types._BaseFieldType):

	__slots__ = ["_FrthrMod", "_Rvvd"]
	@property
	def FrthrMod(self):
		return self._FrthrMod

	@FrthrMod.setter
	def FrthrMod(self, value):
		self._FrthrMod = value if value is not None else base_types.UninitialisedField(self, 'FrthrMod', YesNoIndicator, False)

	@FrthrMod.deleter
	def FrthrMod(self):
		del self._FrthrMod
		self._FrthrMod = base_types.UninitialisedField(self, 'FrthrMod', YesNoIndicator, False)

	@property
	def Rvvd(self):
		return self._Rvvd

	@Rvvd.setter
	def Rvvd(self, value):
		self._Rvvd = value if value is not None else base_types.UninitialisedField(self, 'Rvvd', YesNoIndicator, False)

	@Rvvd.deleter
	def Rvvd(self):
		del self._Rvvd
		self._Rvvd = base_types.UninitialisedField(self, 'Rvvd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrthrMod', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvvd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))