# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralType6Code
from . import ExposureType10Code
from . import Operation3Code

class TradeTypeQueryCriteria2(base_types._BaseFieldType):

	__slots__ = ["_CollCmpntTp", "_Oprtr", "_SctiesFincgTxTp"]
	@property
	def CollCmpntTp(self):
		return self._CollCmpntTp

	@CollCmpntTp.setter
	def CollCmpntTp(self, value):
		self._CollCmpntTp = value if value is not None else base_types.UninitialisedField(self, 'CollCmpntTp', CollateralType6Code, True)

	@CollCmpntTp.deleter
	def CollCmpntTp(self):
		del self._CollCmpntTp
		self._CollCmpntTp = base_types.UninitialisedField(self, 'CollCmpntTp', CollateralType6Code, True)

	@property
	def Oprtr(self):
		return self._Oprtr

	@Oprtr.setter
	def Oprtr(self, value):
		self._Oprtr = value if value is not None else base_types.UninitialisedField(self, 'Oprtr', Operation3Code, False)

	@Oprtr.deleter
	def Oprtr(self):
		del self._Oprtr
		self._Oprtr = base_types.UninitialisedField(self, 'Oprtr', Operation3Code, False)

	@property
	def SctiesFincgTxTp(self):
		return self._SctiesFincgTxTp

	@SctiesFincgTxTp.setter
	def SctiesFincgTxTp(self, value):
		self._SctiesFincgTxTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgTxTp', ExposureType10Code, True)

	@SctiesFincgTxTp.deleter
	def SctiesFincgTxTp(self):
		del self._SctiesFincgTxTp
		self._SctiesFincgTxTp = base_types.UninitialisedField(self, 'SctiesFincgTxTp', ExposureType10Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollCmpntTp', type=CollateralType6Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Oprtr', type=Operation3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgTxTp', type=ExposureType10Code, min=0, max=None, mutex_group=None, array=True),
	))