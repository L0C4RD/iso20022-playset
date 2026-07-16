# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentifier
from . import PartyIdentification26

class PartyIdentification29Choice(base_types._BaseFieldType):

	__slots__ = ["_BIC", "_NmAndAdr"]
	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if value is not None else base_types.UninitialisedField(self, 'BIC', BICIdentifier, False)

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = base_types.UninitialisedField(self, 'BIC', BICIdentifier, False)

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', PartyIdentification26, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', PartyIdentification26, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BIC', type=BICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=PartyIdentification26, min=0, max=1, mutex_group=1, array=False),
	))