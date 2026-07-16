# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BillingMethod1
from . import BillingMethod2
from . import BillingMethod3

class BillingMethod1Choice(base_types._BaseFieldType):

	__slots__ = ["_MtdA", "_MtdB", "_MtdD"]
	@property
	def MtdA(self):
		return self._MtdA

	@MtdA.setter
	def MtdA(self, value):
		self._MtdA = value if value is not None else base_types.UninitialisedField(self, 'MtdA', BillingMethod1, False)

	@MtdA.deleter
	def MtdA(self):
		del self._MtdA
		self._MtdA = base_types.UninitialisedField(self, 'MtdA', BillingMethod1, False)

	@property
	def MtdB(self):
		return self._MtdB

	@MtdB.setter
	def MtdB(self, value):
		self._MtdB = value if value is not None else base_types.UninitialisedField(self, 'MtdB', BillingMethod2, False)

	@MtdB.deleter
	def MtdB(self):
		del self._MtdB
		self._MtdB = base_types.UninitialisedField(self, 'MtdB', BillingMethod2, False)

	@property
	def MtdD(self):
		return self._MtdD

	@MtdD.setter
	def MtdD(self, value):
		self._MtdD = value if value is not None else base_types.UninitialisedField(self, 'MtdD', BillingMethod3, False)

	@MtdD.deleter
	def MtdD(self):
		del self._MtdD
		self._MtdD = base_types.UninitialisedField(self, 'MtdD', BillingMethod3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtdA', type=BillingMethod1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtdB', type=BillingMethod2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtdD', type=BillingMethod3, min=0, max=1, mutex_group=1, array=False),
	))