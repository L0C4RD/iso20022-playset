# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AnyBICDec2014Identifier
from . import LEIIdentifier
from . import Max50Text
from . import NotReported1Code

class TradePartyIdentificationQuery8(base_types._BaseFieldType):

	__slots__ = ["_AnyBIC", "_ClntId", "_LEI", "_NotRptd"]
	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if value is not None else base_types.UninitialisedField(self, 'AnyBIC', AnyBICDec2014Identifier, True)

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = base_types.UninitialisedField(self, 'AnyBIC', AnyBICDec2014Identifier, True)

	@property
	def ClntId(self):
		return self._ClntId

	@ClntId.setter
	def ClntId(self, value):
		self._ClntId = value if value is not None else base_types.UninitialisedField(self, 'ClntId', Max50Text, True)

	@ClntId.deleter
	def ClntId(self):
		del self._ClntId
		self._ClntId = base_types.UninitialisedField(self, 'ClntId', Max50Text, True)

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if value is not None else base_types.UninitialisedField(self, 'LEI', LEIIdentifier, True)

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = base_types.UninitialisedField(self, 'LEI', LEIIdentifier, True)

	@property
	def NotRptd(self):
		return self._NotRptd

	@NotRptd.setter
	def NotRptd(self, value):
		self._NotRptd = value if value is not None else base_types.UninitialisedField(self, 'NotRptd', NotReported1Code, False)

	@NotRptd.deleter
	def NotRptd(self):
		del self._NotRptd
		self._NotRptd = base_types.UninitialisedField(self, 'NotRptd', NotReported1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyBIC', type=AnyBICDec2014Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClntId', type=Max50Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NotRptd', type=NotReported1Code, min=0, max=1, mutex_group=None, array=False),
	))