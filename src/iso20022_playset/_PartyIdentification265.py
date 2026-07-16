# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICDec2014Identifier
from . import Max35Text

class PartyIdentification265(base_types._BaseFieldType):

	__slots__ = ["_AltrntvIdr", "_AnyBIC"]
	@property
	def AltrntvIdr(self):
		return self._AltrntvIdr

	@AltrntvIdr.setter
	def AltrntvIdr(self, value):
		self._AltrntvIdr = value if value is not None else base_types.UninitialisedField(self, 'AltrntvIdr', Max35Text, True)

	@AltrntvIdr.deleter
	def AltrntvIdr(self):
		del self._AltrntvIdr
		self._AltrntvIdr = base_types.UninitialisedField(self, 'AltrntvIdr', Max35Text, True)

	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if value is not None else base_types.UninitialisedField(self, 'AnyBIC', AnyBICDec2014Identifier, False)

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = base_types.UninitialisedField(self, 'AnyBIC', AnyBICDec2014Identifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrntvIdr', type=Max35Text, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=1, max=1, mutex_group=None, array=False),
	))