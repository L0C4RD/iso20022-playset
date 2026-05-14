# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DigitalPaymentSettlement3 import DigitalPaymentSettlement3
from ._Fee9 import Fee9
from ._Max35Text import Max35Text
from ._Tax42 import Tax42

class FeeAndTax2(base_types._BaseFieldType):

	__slots__ = ["_ComrclAgrmtRef", "_DgtlNtwkFee", "_IndvFee", "_IndvTax"]
	@property
	def ComrclAgrmtRef(self):
		return self._ComrclAgrmtRef

	@ComrclAgrmtRef.setter
	def ComrclAgrmtRef(self, value):
		self._ComrclAgrmtRef = value if type(value) != base_types.auto else self.make_default("ComrclAgrmtRef")

	@ComrclAgrmtRef.deleter
	def ComrclAgrmtRef(self):
		del self._ComrclAgrmtRef
		self._ComrclAgrmtRef = None

	@property
	def DgtlNtwkFee(self):
		return self._DgtlNtwkFee

	@DgtlNtwkFee.setter
	def DgtlNtwkFee(self, value):
		self._DgtlNtwkFee = value if type(value) != base_types.auto else self.make_default("DgtlNtwkFee")

	@DgtlNtwkFee.deleter
	def DgtlNtwkFee(self):
		del self._DgtlNtwkFee
		self._DgtlNtwkFee = None

	@property
	def IndvFee(self):
		return self._IndvFee

	@IndvFee.setter
	def IndvFee(self, value):
		self._IndvFee = value if type(value) != base_types.auto else self.make_default("IndvFee")

	@IndvFee.deleter
	def IndvFee(self):
		del self._IndvFee
		self._IndvFee = None

	@property
	def IndvTax(self):
		return self._IndvTax

	@IndvTax.setter
	def IndvTax(self, value):
		self._IndvTax = value if type(value) != base_types.auto else self.make_default("IndvTax")

	@IndvTax.deleter
	def IndvTax(self):
		del self._IndvTax
		self._IndvTax = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComrclAgrmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlNtwkFee', type=DigitalPaymentSettlement3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IndvFee', type=Fee9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IndvTax', type=Tax42, min=0, max=None, mutex_group=None, array=True),
	))