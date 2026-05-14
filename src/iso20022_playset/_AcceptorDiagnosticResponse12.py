# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardPaymentEnvironment82 import CardPaymentEnvironment82
from ._TMSTrigger1 import TMSTrigger1
from ._TrueFalseIndicator import TrueFalseIndicator

class AcceptorDiagnosticResponse12(base_types._BaseFieldType):

	__slots__ = ["_AcqrrAvlbl", "_Envt", "_TMSTrggr"]
	@property
	def AcqrrAvlbl(self):
		return self._AcqrrAvlbl

	@AcqrrAvlbl.setter
	def AcqrrAvlbl(self, value):
		self._AcqrrAvlbl = value if type(value) != base_types.auto else self.make_default("AcqrrAvlbl")

	@AcqrrAvlbl.deleter
	def AcqrrAvlbl(self):
		del self._AcqrrAvlbl
		self._AcqrrAvlbl = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def TMSTrggr(self):
		return self._TMSTrggr

	@TMSTrggr.setter
	def TMSTrggr(self, value):
		self._TMSTrggr = value if type(value) != base_types.auto else self.make_default("TMSTrggr")

	@TMSTrggr.deleter
	def TMSTrggr(self):
		del self._TMSTrggr
		self._TMSTrggr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrAvlbl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSTrggr', type=TMSTrigger1, min=0, max=1, mutex_group=None, array=False),
	))