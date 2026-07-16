# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification5
from . import MICIdentifier
from . import PriceSource

class PriceSourceFormatChoice(base_types._BaseFieldType):

	__slots__ = ["_LclMktPlc", "_NonLclMktPlc", "_PlcAsDSS"]
	@property
	def LclMktPlc(self):
		return self._LclMktPlc

	@LclMktPlc.setter
	def LclMktPlc(self, value):
		self._LclMktPlc = value if value is not None else base_types.UninitialisedField(self, 'LclMktPlc', MICIdentifier, False)

	@LclMktPlc.deleter
	def LclMktPlc(self):
		del self._LclMktPlc
		self._LclMktPlc = base_types.UninitialisedField(self, 'LclMktPlc', MICIdentifier, False)

	@property
	def NonLclMktPlc(self):
		return self._NonLclMktPlc

	@NonLclMktPlc.setter
	def NonLclMktPlc(self, value):
		self._NonLclMktPlc = value if value is not None else base_types.UninitialisedField(self, 'NonLclMktPlc', PriceSource, False)

	@NonLclMktPlc.deleter
	def NonLclMktPlc(self):
		del self._NonLclMktPlc
		self._NonLclMktPlc = base_types.UninitialisedField(self, 'NonLclMktPlc', PriceSource, False)

	@property
	def PlcAsDSS(self):
		return self._PlcAsDSS

	@PlcAsDSS.setter
	def PlcAsDSS(self, value):
		self._PlcAsDSS = value if value is not None else base_types.UninitialisedField(self, 'PlcAsDSS', GenericIdentification5, False)

	@PlcAsDSS.deleter
	def PlcAsDSS(self):
		del self._PlcAsDSS
		self._PlcAsDSS = base_types.UninitialisedField(self, 'PlcAsDSS', GenericIdentification5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LclMktPlc', type=MICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NonLclMktPlc', type=PriceSource, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PlcAsDSS', type=GenericIdentification5, min=0, max=1, mutex_group=1, array=False),
	))