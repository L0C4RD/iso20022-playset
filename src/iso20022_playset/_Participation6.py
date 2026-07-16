# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity18Choice
from . import ISODate
from . import Number
from . import Percentage14Rate

class Participation6(base_types._BaseFieldType):

	__slots__ = ["_ClctnDt", "_PctgOfVtngRghts", "_TtlNbOfSctiesOutsdng", "_TtlNbOfVtngRghts"]
	@property
	def ClctnDt(self):
		return self._ClctnDt

	@ClctnDt.setter
	def ClctnDt(self, value):
		self._ClctnDt = value if value is not None else base_types.UninitialisedField(self, 'ClctnDt', ISODate, False)

	@ClctnDt.deleter
	def ClctnDt(self):
		del self._ClctnDt
		self._ClctnDt = base_types.UninitialisedField(self, 'ClctnDt', ISODate, False)

	@property
	def PctgOfVtngRghts(self):
		return self._PctgOfVtngRghts

	@PctgOfVtngRghts.setter
	def PctgOfVtngRghts(self, value):
		self._PctgOfVtngRghts = value if value is not None else base_types.UninitialisedField(self, 'PctgOfVtngRghts', Percentage14Rate, False)

	@PctgOfVtngRghts.deleter
	def PctgOfVtngRghts(self):
		del self._PctgOfVtngRghts
		self._PctgOfVtngRghts = base_types.UninitialisedField(self, 'PctgOfVtngRghts', Percentage14Rate, False)

	@property
	def TtlNbOfSctiesOutsdng(self):
		return self._TtlNbOfSctiesOutsdng

	@TtlNbOfSctiesOutsdng.setter
	def TtlNbOfSctiesOutsdng(self, value):
		self._TtlNbOfSctiesOutsdng = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfSctiesOutsdng', FinancialInstrumentQuantity18Choice, False)

	@TtlNbOfSctiesOutsdng.deleter
	def TtlNbOfSctiesOutsdng(self):
		del self._TtlNbOfSctiesOutsdng
		self._TtlNbOfSctiesOutsdng = base_types.UninitialisedField(self, 'TtlNbOfSctiesOutsdng', FinancialInstrumentQuantity18Choice, False)

	@property
	def TtlNbOfVtngRghts(self):
		return self._TtlNbOfVtngRghts

	@TtlNbOfVtngRghts.setter
	def TtlNbOfVtngRghts(self, value):
		self._TtlNbOfVtngRghts = value if value is not None else base_types.UninitialisedField(self, 'TtlNbOfVtngRghts', Number, False)

	@TtlNbOfVtngRghts.deleter
	def TtlNbOfVtngRghts(self):
		del self._TtlNbOfVtngRghts
		self._TtlNbOfVtngRghts = base_types.UninitialisedField(self, 'TtlNbOfVtngRghts', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfVtngRghts', type=Percentage14Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfSctiesOutsdng', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNbOfVtngRghts', type=Number, min=0, max=1, mutex_group=None, array=False),
	))