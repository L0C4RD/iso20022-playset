# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification127Choice
from . import PartyIdentificationAndAccount149

class Clearing5(base_types._BaseFieldType):

	__slots__ = ["_ClrMmb", "_ClrSgmt"]
	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if value is not None else base_types.UninitialisedField(self, 'ClrMmb', PartyIdentificationAndAccount149, True)

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = base_types.UninitialisedField(self, 'ClrMmb', PartyIdentificationAndAccount149, True)

	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if value is not None else base_types.UninitialisedField(self, 'ClrSgmt', PartyIdentification127Choice, False)

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = base_types.UninitialisedField(self, 'ClrSgmt', PartyIdentification127Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentificationAndAccount149, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification127Choice, min=0, max=1, mutex_group=None, array=False),
	))