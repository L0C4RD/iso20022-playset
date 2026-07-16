# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification1
from . import Max140Text
from . import ProcessingType1Choice

class BalanceRestrictionType1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_PrcgTp", "_Tp"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@property
	def PrcgTp(self):
		return self._PrcgTp

	@PrcgTp.setter
	def PrcgTp(self, value):
		self._PrcgTp = value if value is not None else base_types.UninitialisedField(self, 'PrcgTp', ProcessingType1Choice, False)

	@PrcgTp.deleter
	def PrcgTp(self):
		del self._PrcgTp
		self._PrcgTp = base_types.UninitialisedField(self, 'PrcgTp', ProcessingType1Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', GenericIdentification1, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', GenericIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgTp', type=ProcessingType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=GenericIdentification1, min=1, max=1, mutex_group=None, array=False),
	))