# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DistributionStrategy1Choice
from . import OtherDistributionStrategy1

class DistributionStrategy1(base_types._BaseFieldType):

	__slots__ = ["_ExctnOnly", "_ExctnWthApprprtnssTstOrNonAdvsdSvcs", "_InvstmtAdvc", "_Othr", "_PrtflMgmt"]
	@property
	def ExctnOnly(self):
		return self._ExctnOnly

	@ExctnOnly.setter
	def ExctnOnly(self, value):
		self._ExctnOnly = value if value is not None else base_types.UninitialisedField(self, 'ExctnOnly', DistributionStrategy1Choice, False)

	@ExctnOnly.deleter
	def ExctnOnly(self):
		del self._ExctnOnly
		self._ExctnOnly = base_types.UninitialisedField(self, 'ExctnOnly', DistributionStrategy1Choice, False)

	@property
	def ExctnWthApprprtnssTstOrNonAdvsdSvcs(self):
		return self._ExctnWthApprprtnssTstOrNonAdvsdSvcs

	@ExctnWthApprprtnssTstOrNonAdvsdSvcs.setter
	def ExctnWthApprprtnssTstOrNonAdvsdSvcs(self, value):
		self._ExctnWthApprprtnssTstOrNonAdvsdSvcs = value if value is not None else base_types.UninitialisedField(self, 'ExctnWthApprprtnssTstOrNonAdvsdSvcs', DistributionStrategy1Choice, False)

	@ExctnWthApprprtnssTstOrNonAdvsdSvcs.deleter
	def ExctnWthApprprtnssTstOrNonAdvsdSvcs(self):
		del self._ExctnWthApprprtnssTstOrNonAdvsdSvcs
		self._ExctnWthApprprtnssTstOrNonAdvsdSvcs = base_types.UninitialisedField(self, 'ExctnWthApprprtnssTstOrNonAdvsdSvcs', DistributionStrategy1Choice, False)

	@property
	def InvstmtAdvc(self):
		return self._InvstmtAdvc

	@InvstmtAdvc.setter
	def InvstmtAdvc(self, value):
		self._InvstmtAdvc = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAdvc', DistributionStrategy1Choice, False)

	@InvstmtAdvc.deleter
	def InvstmtAdvc(self):
		del self._InvstmtAdvc
		self._InvstmtAdvc = base_types.UninitialisedField(self, 'InvstmtAdvc', DistributionStrategy1Choice, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', OtherDistributionStrategy1, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', OtherDistributionStrategy1, False)

	@property
	def PrtflMgmt(self):
		return self._PrtflMgmt

	@PrtflMgmt.setter
	def PrtflMgmt(self, value):
		self._PrtflMgmt = value if value is not None else base_types.UninitialisedField(self, 'PrtflMgmt', DistributionStrategy1Choice, False)

	@PrtflMgmt.deleter
	def PrtflMgmt(self):
		del self._PrtflMgmt
		self._PrtflMgmt = base_types.UninitialisedField(self, 'PrtflMgmt', DistributionStrategy1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ExctnOnly', type=DistributionStrategy1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnWthApprprtnssTstOrNonAdvsdSvcs', type=DistributionStrategy1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAdvc', type=DistributionStrategy1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherDistributionStrategy1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflMgmt', type=DistributionStrategy1Choice, min=0, max=1, mutex_group=None, array=False),
	))