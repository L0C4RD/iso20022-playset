# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OptionDateOrPeriod1Choice
from . import OptionType1Code

class Option12(base_types._BaseFieldType):

	__slots__ = ["_DtOrPrd", "_Tp"]
	@property
	def DtOrPrd(self):
		return self._DtOrPrd

	@DtOrPrd.setter
	def DtOrPrd(self, value):
		self._DtOrPrd = value if value is not None else base_types.UninitialisedField(self, 'DtOrPrd', OptionDateOrPeriod1Choice, False)

	@DtOrPrd.deleter
	def DtOrPrd(self):
		del self._DtOrPrd
		self._DtOrPrd = base_types.UninitialisedField(self, 'DtOrPrd', OptionDateOrPeriod1Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', OptionType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', OptionType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtOrPrd', type=OptionDateOrPeriod1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=OptionType1Code, min=1, max=1, mutex_group=None, array=False),
	))