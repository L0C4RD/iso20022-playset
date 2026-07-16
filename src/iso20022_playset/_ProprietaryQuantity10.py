# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Exact4AlphaNumericText
from . import Max4AlphaNumericText
from . import RestrictedFINDecimalNumber
from . import ShortLong1Code

class ProprietaryQuantity10(base_types._BaseFieldType):

	__slots__ = ["_Issr", "_Qty", "_QtyTp", "_SchmeNm", "_ShrtLngPos"]
	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', Max4AlphaNumericText, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', Max4AlphaNumericText, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', RestrictedFINDecimalNumber, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', RestrictedFINDecimalNumber, False)

	@property
	def QtyTp(self):
		return self._QtyTp

	@QtyTp.setter
	def QtyTp(self, value):
		self._QtyTp = value if value is not None else base_types.UninitialisedField(self, 'QtyTp', Exact4AlphaNumericText, False)

	@QtyTp.deleter
	def QtyTp(self):
		del self._QtyTp
		self._QtyTp = base_types.UninitialisedField(self, 'QtyTp', Exact4AlphaNumericText, False)

	@property
	def SchmeNm(self):
		return self._SchmeNm

	@SchmeNm.setter
	def SchmeNm(self, value):
		self._SchmeNm = value if value is not None else base_types.UninitialisedField(self, 'SchmeNm', Max4AlphaNumericText, False)

	@SchmeNm.deleter
	def SchmeNm(self):
		del self._SchmeNm
		self._SchmeNm = base_types.UninitialisedField(self, 'SchmeNm', Max4AlphaNumericText, False)

	@property
	def ShrtLngPos(self):
		return self._ShrtLngPos

	@ShrtLngPos.setter
	def ShrtLngPos(self, value):
		self._ShrtLngPos = value if value is not None else base_types.UninitialisedField(self, 'ShrtLngPos', ShortLong1Code, False)

	@ShrtLngPos.deleter
	def ShrtLngPos(self):
		del self._ShrtLngPos
		self._ShrtLngPos = base_types.UninitialisedField(self, 'ShrtLngPos', ShortLong1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Issr', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=RestrictedFINDecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyTp', type=Exact4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchmeNm', type=Max4AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtLngPos', type=ShortLong1Code, min=0, max=1, mutex_group=None, array=False),
	))