# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActionMessage12
from . import RetailerService2Code
from . import TransactionAction1Code

class EnableServiceRequest7(base_types._BaseFieldType):

	__slots__ = ["_DispOutpt", "_SvcsNbld", "_TxActn"]
	@property
	def DispOutpt(self):
		return self._DispOutpt

	@DispOutpt.setter
	def DispOutpt(self, value):
		self._DispOutpt = value if value is not None else base_types.UninitialisedField(self, 'DispOutpt', ActionMessage12, False)

	@DispOutpt.deleter
	def DispOutpt(self):
		del self._DispOutpt
		self._DispOutpt = base_types.UninitialisedField(self, 'DispOutpt', ActionMessage12, False)

	@property
	def SvcsNbld(self):
		return self._SvcsNbld

	@SvcsNbld.setter
	def SvcsNbld(self, value):
		self._SvcsNbld = value if value is not None else base_types.UninitialisedField(self, 'SvcsNbld', RetailerService2Code, False)

	@SvcsNbld.deleter
	def SvcsNbld(self):
		del self._SvcsNbld
		self._SvcsNbld = base_types.UninitialisedField(self, 'SvcsNbld', RetailerService2Code, False)

	@property
	def TxActn(self):
		return self._TxActn

	@TxActn.setter
	def TxActn(self, value):
		self._TxActn = value if value is not None else base_types.UninitialisedField(self, 'TxActn', TransactionAction1Code, False)

	@TxActn.deleter
	def TxActn(self):
		del self._TxActn
		self._TxActn = base_types.UninitialisedField(self, 'TxActn', TransactionAction1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DispOutpt', type=ActionMessage12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcsNbld', type=RetailerService2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxActn', type=TransactionAction1Code, min=1, max=1, mutex_group=None, array=False),
	))